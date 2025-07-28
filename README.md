# Quesera Chatbot

Quesera Chatbot is a lightweight, privacy-focused AI assistant powered by the Phi-3 language model running locally via Ollama. Built using Flask and integrated with a clean frontend UI, the chatbot is designed to deliver fast and contextual responses without relying on any cloud-based APIs.

# Features

* Local LLM Integration (Phi-3 via Ollama)
* Conversational AI with instant response generation
* Lightweight and browser-accessible UI using HTML/CSS/JS
* Zero dependency on OpenAI API or internet access for inference
* Easy to modify prompts and extend capabilities

# Technologies Used

* Python 3
* Flask
* HTML, CSS, JavaScript
* Ollama (for running the Phi-3 model locally)

# Setup Instructions

* Python 3.x
* Ollama installed and running (`ollama run phi3`)

# 1. Clone the Repository

git clone https://github.com/Adityabhatia0204/quesera-chatbot.git
cd quesera-chatbot

# 2. Install Python Dependencies

pip install -r requirements.txt

# 3. Start the Chatbot UI Server

python main.py

Visit `http://localhost:5001` in your browser to access the chatbot interface.

# How It Works

* The user types a message in the web interface.
* The message is sent via a POST request to the Flask backend.
* Flask makes a local API call to `http://localhost:11434/api/generate` using the Phi-3 model.
* The response is returned and displayed in the chat interface.


# Sample Prompt

User: What's the capital of Italy?
Bot: The capital of Italy is Rome.

# Notes

* This project is intended for local use and demonstration purposes.
* You can modify the prompt structure inside `main.py` to customize chatbot behavior.


Built by Aditya Bhatia ❤️
