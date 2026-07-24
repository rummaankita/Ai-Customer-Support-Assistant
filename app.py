"""
app.py
------
This is the main Flask web server for our AI Customer Support Assistant.

What this file does:
1. Starts a Flask web application.
2. Shows the chat webpage (index.html) to the user.
3. Listens for chat messages sent from the browser (via JavaScript).
4. Passes the user's message to chatbot.py to get an AI reply.
5. Sends that AI reply back to the browser as JSON.

How it connects with other files:
- templates/index.html -> the webpage shown to the user (served by this file)
- static/style.css / static/script.js -> loaded automatically by index.html
- chatbot.py -> used here to generate the actual AI response
- .env -> read indirectly through chatbot.py (which loads the Gemini API key)
"""

from flask import Flask, render_template, request, jsonify
from chatbot import get_ai_response

# Create the Flask application
app = Flask(__name__)


@app.route("/")
def home():
    """
    This route shows the main chat webpage when the user visits the site.
    Flask automatically looks for 'index.html' inside the 'templates' folder.
    """
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    """
    This route receives the user's message from the frontend (script.js),
    sends it to the Gemini AI model (through chatbot.py), and returns
    the AI's reply as a JSON response.
    """
    # Get the JSON data sent from the browser
    data = request.get_json()

    # Safely extract the "message" field, defaulting to an empty string
    user_message = data.get("message", "").strip() if data else ""

    # Basic server-side safety check: don't process empty messages
    if not user_message:
        return jsonify({"reply": "Please type a message before sending."})

    # Get the AI-generated reply from chatbot.py
    ai_reply = get_ai_response(user_message)

    # Send the reply back to the frontend as JSON
    return jsonify({"reply": ai_reply})


# This makes sure the server only runs when this file is executed directly
# (not when it's imported somewhere else).
if __name__ == "__main__":
    # debug=True gives helpful error messages while developing.
    # Turn this off (debug=False) before deploying to a real server.
    app.run(debug=True)
