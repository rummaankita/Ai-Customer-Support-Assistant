# 🤖 AI Customer Support Assistant

A simple,  AI-powered customer support chatbot built with
**Python Flask**, **HTML/CSS/JavaScript**, and the **Groq API** (running
Llama 3.3 for fast, free AI responses).

This project is designed to be easy to understand and explain — perfect for
a B.Tech CSE student learning how AI, web backends, and frontends connect
together.

---

## 📖 Project Overview

The AI Customer Support Assistant is a web-based chatbot that:
- Greets the user with a friendly welcome message.
- Lets the user type questions in a chat box.
- Sends those questions to Groq's AI model (Llama 3.3).
- Displays the AI's response in a clean chat bubble.
- Shows a loading indicator while waiting for a reply.
- Handles errors gracefully if the AI API fails.

No database, no frameworks like Bootstrap/React/LangChain — just plain
Flask + HTML + CSS + JavaScript, so every line of code is easy to read.

---

## 📁 Folder Structure

```
AI-Customer-Support-Assistant/
│── app.py                 # Flask backend server (routes)
│── chatbot.py              # Handles communication with the Groq AI API
│── requirements.txt         # List of required Python packages
│── .env                     # Stores your secret Groq API key
│── templates/
│   └── index.html           # Chatbot webpage structure
│── static/
│   ├── style.css             # Chatbot styling (blue & white theme)
│   ├── script.js              # Chatbot interactivity (JavaScript)
|--images/
|   |--chatbot-output.png
│── README.md                # This file
```

---

## ⚙️ Installation Steps

### 1. Install Python
Make sure you have **Python 3.9+** installed. Check with:
```bash
python --version
```
(If that fails on Windows, use `py --version` instead.)

### 2. Open the project in VS Code
Open the `AI-Customer-Support-Assistant` folder in VS Code.

### 3. Create a virtual environment (recommended)
```bash
python -m venv venv
```

Activate it:
- **Windows (PowerShell):** `venv\Scripts\activate`
- **Mac/Linux:** `source venv/bin/activate`

> If Windows blocks the script with a "running scripts is disabled" error, run
> this once: `Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned`

You'll know it worked when you see `(venv)` at the start of your terminal line.

### 4. Install required packages
```bash
pip install -r requirements.txt
```

---

## 📦 Required Packages

These are listed in `requirements.txt`:

| Package | Purpose |
|---|---|
| `Flask` | Runs the web server and handles routes |
| `python-dotenv` | Loads the Groq API key from the `.env` file |
| `groq` | Official Groq library used to talk to the AI model |

---

## 🔑 How to Add Your Groq API Key

1. Go to **[Groq Console](https://console.groq.com/keys)** and sign in
   (a Google account works fine).
2. Click **"Create API Key"**, name it anything, and copy the key
   (it starts with `gsk_...`).
3. Open the `.env` file in the project folder.
4. Replace the placeholder with your real key:

```
GROQ_API_KEY=gsk_your_actual_key_here
```

⚠️ **Never share your `.env` file publicly** (e.g., don't upload it to GitHub)
— it contains your private API key.

---

## ▶️ How to Run the Project in VS Code

1. Open a terminal in VS Code (`Ctrl + ~` or `View > Terminal`).
2. Make sure your virtual environment is activated — you should see `(venv)`.
3. Run the Flask app:
   ```bash
   python app.py
   ```
4. You should see output like:
   ```
   * Running on http://127.0.0.1:5000
   ```
5. Open your browser and go to:
   ```
   http://127.0.0.1:5000
   ```
6. The chatbot page will load, greet you, and you can start chatting!

To stop the server, click back in the terminal and press `Ctrl + C`.

---

## ✅ Expected Output

- A clean, blue-and-white chat interface opens in your browser.
- A greeting message appears automatically: *"👋 Hello! I'm your AI Customer
  Support Assistant. How can I help you today?"*
- Typing a message and pressing **Enter** (or clicking **Send**) shows your
  message in a blue bubble on the right.
- After a short loading animation (bouncing dots), the AI's reply appears
  in a light-blue bubble on the left — usually within a second, since Groq
  is extremely fast.
- The chat automatically scrolls down as new messages appear.
- If something goes wrong (e.g., invalid API key, no internet), a red error
  bubble appears instead of crashing the page.

---

## 🛠️ Troubleshooting Tips

| Problem | Likely Cause | Solution |
|---|---|---|
| `ModuleNotFoundError: No module named 'flask'` or `'groq'` | Packages not installed | Run `pip install -r requirements.txt` |
| Chatbot always replies "having trouble responding" | Invalid/missing Groq API key | Check `.env` has the correct `GROQ_API_KEY`, no extra spaces or quotes |
| `[Groq API Error]: 401 ...` in terminal | Wrong or expired API key | Generate a new key at [console.groq.com/keys](https://console.groq.com/keys) |
| `python` not recognized (Windows) | Python not installed or not in PATH | Reinstall Python and check "Add python.exe to PATH" during setup |
| `running scripts is disabled` when activating venv | Windows PowerShell security setting | Run: `Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned` |
| Page shows "Not Found" or won't load | `app.py` isn't running, or wrong URL | Make sure `python app.py` is running, and visit `http://127.0.0.1:5000` |
| Changes to CSS/JS not showing | Browser cache | Hard refresh with `Ctrl + Shift + R` |
| `.env` values not loading | File misnamed or misplaced | Ensure it's named exactly `.env` and sits in the project's root folder |

---

## 🧩 How the Files Work Together

1. **User opens the browser** → Flask (`app.py`) serves `templates/index.html`.
2. **`index.html`** loads `static/style.css` (for looks) and `static/script.js`
   (for behavior).
3. **User types a message and hits Enter/Send** → `script.js` sends it to the
   `/chat` route in `app.py` using `fetch()`.
4. **`app.py`** receives the message and passes it to `chatbot.py`.
5. **`chatbot.py`** reads the API key from `.env`, sends the message to the
   **Groq API** (Llama 3.3 model), and returns the AI's reply.
6. **`app.py`** sends that reply back to `script.js` as JSON.
7. **`script.js`** displays the reply in a chat bubble on the page.

This is the complete request-response cycle of the chatbot! 🎉

---

## 📚 Tech Stack Summary

- **Backend:** Python, Flask
- **Frontend:** HTML, CSS, JavaScript (no frameworks)
- **AI Model:** Groq API — `llama-3.3-70b-versatile`
- **Config Management:** `python-dotenv`

---

Made with ❤️ for learning how AI + Web Development work together.