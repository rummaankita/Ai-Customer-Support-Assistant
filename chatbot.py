"""
chatbot.py
----------
This file is responsible for talking to the Groq AI API.
It takes a user's message, sends it to Groq, and returns the AI's reply.
 
Keeping this logic in a separate file (instead of putting it inside app.py)
makes the project cleaner and easier to understand:
- app.py handles the WEB SERVER (routes, requests, responses)
- chatbot.py handles the AI LOGIC (talking to Groq)
"""
 
import os
from groq import Groq
from dotenv import load_dotenv
 
# Load environment variables from the .env file (this is where our API key lives)
load_dotenv()
 
# Read the Groq API key securely from the .env file
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
 
# Create the Groq client once, using our API key
client = Groq(api_key=GROQ_API_KEY)
 
# The model we want to use. "openai/gpt-oss-120b" is Groq's current
# recommended general-purpose model (as of mid-2026). Note: the older
# "llama-3.3-70b-versatile" model was deprecated by Groq in June 2026.
MODEL_NAME = "openai/gpt-oss-120b"
 
# A "system instruction" tells the AI how to behave.
SYSTEM_INSTRUCTION = (
    "You are a professional and friendly AI Customer Support Assistant for "
    "a business. Only help with customer support topics such as orders, "
    "returns, refunds, shipping, billing, account issues, product questions, "
    "and complaints. Always answer politely, clearly, and concisely, like a "
    "real support agent would. "
    "If the user asks something unrelated to customer support (for example, "
    "general knowledge, coding help, or personal advice), politely let them "
    "know that you are a customer support assistant and can only help with "
    "support-related questions, then invite them to ask something related "
    "to their order, account, or product instead. "
    "If you don't know the answer to a genuine support question, politely "
    "say so and suggest the user contact human support for further help."
)
 
 
def get_ai_response(user_message):
    """
    Sends the user's message to Groq and returns the AI's text reply.
 
    Parameters:
        user_message (str): The message typed by the user.
 
    Returns:
        str: The AI-generated reply, or an error message if something goes wrong.
    """
    try:
        # Ask Groq to generate a response based on the user's message.
        # We send two messages: a "system" message (the AI's instructions)
        # and a "user" message (what the person actually typed).
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {"role": "system", "content": SYSTEM_INSTRUCTION},
                {"role": "user", "content": user_message},
            ],
        )
 
        # Return just the text part of the response
        return response.choices[0].message.content.strip()
 
    except Exception as error:
        # If anything goes wrong (bad API key, no internet, server issue, etc.)
        # we print the real error in the terminal for debugging...
        print(f"[Groq API Error]: {error}")
 
        # ...but show a friendly, non-technical message to the user.
        return (
            "Sorry, I'm having trouble responding right now. "
            "Please try again in a moment."
        )
