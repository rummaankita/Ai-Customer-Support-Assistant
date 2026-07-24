/* ==========================================================
   script.js
   ----------
   This file controls the BEHAVIOR of our chatbot:
   sending messages, showing replies, loading indicator,
   error handling, and auto-scrolling.
   ========================================================== */

// Grab references to the HTML elements we need to work with
const chatMessages = document.getElementById("chat-messages");
const userInput = document.getElementById("user-input");
const sendButton = document.getElementById("send-button");
const loadingIndicator = document.getElementById("loading-indicator");

/**
 * Adds a new message bubble to the chat window.
 * @param {string} text - The message text to display.
 * @param {string} sender - "user", "ai", or "error" (controls bubble color).
 */
function addMessage(text, sender) {
    const messageDiv = document.createElement("div");

    // Choose the correct CSS class based on who sent the message
    if (sender === "user") {
        messageDiv.classList.add("message", "user-message");
    } else if (sender === "error") {
        messageDiv.classList.add("message", "error-message");
    } else {
        messageDiv.classList.add("message", "ai-message");
    }

    messageDiv.textContent = text;
    chatMessages.appendChild(messageDiv);

    // Automatically scroll to the latest message
    scrollToBottom();
}

/**
 * Scrolls the chat window down to the most recent message.
 */
function scrollToBottom() {
    chatMessages.scrollTop = chatMessages.scrollHeight;
}

/**
 * Shows or hides the "typing..." loading indicator.
 * @param {boolean} show - true to show it, false to hide it.
 */
function toggleLoading(show) {
    loadingIndicator.style.display = show ? "flex" : "none";
    if (show) scrollToBottom();
}

/**
 * Sends the user's message to the Flask backend (/chat route)
 * and displays the AI's reply once it arrives.
 */
async function sendMessage() {
    const message = userInput.value.trim();

    // Prevent sending empty messages
    if (message === "") {
        return;
    }

    // Show the user's message immediately
    addMessage(message, "user");

    // Clear the input box and disable it while waiting for a reply
    userInput.value = "";
    userInput.disabled = true;
    sendButton.disabled = true;

    // Show the loading indicator (three bouncing dots)
    toggleLoading(true);

    try {
        // Send the message to our Flask backend as JSON
        const response = await fetch("/chat", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ message: message }),
        });

        // If the server responds with an error status, treat it as a failure
        if (!response.ok) {
            throw new Error("Server error");
        }

        const data = await response.json();

        // Display the AI's reply
        addMessage(data.reply, "ai");

    } catch (error) {
        // Show a friendly error bubble if the API call fails
        // (e.g. no internet connection, server not running, etc.)
        console.error("Chat request failed:", error);
        addMessage(
            "Oops! Something went wrong while contacting the assistant. Please try again.",
            "error"
        );
    } finally {
        // Hide the loading indicator and re-enable the input box
        toggleLoading(false);
        userInput.disabled = false;
        sendButton.disabled = false;
        userInput.focus();
    }
}

/* ---------- Event Listeners ---------- */

// Send message when the Send button is clicked
sendButton.addEventListener("click", sendMessage);

// Send message when the user presses Enter inside the input box
userInput.addEventListener("keydown", function (event) {
    if (event.key === "Enter") {
        event.preventDefault();
        sendMessage();
    }
});

/* ---------- Friendly greeting shown when the page loads ---------- */
window.addEventListener("DOMContentLoaded", function () {
    addMessage(
        "👋 Hello! I'm your AI Customer Support Assistant. How can I help you today?",
        "ai"
    );
    userInput.focus();
});
