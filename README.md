# 🤖 Local AI Chatbot using LangChain, Ollama & TinyLlama

## 📌 Project Overview

This project is a **Local AI Chatbot** built using **Python, LangChain, and Ollama**, powered by the **TinyLlama Large Language Model (LLM)**.

Unlike cloud-based AI assistants, this chatbot runs entirely on a local machine, ensuring:

* Data privacy
* Offline accessibility
* Low-latency responses
* No dependency on paid API services

The application supports multi-turn conversations by maintaining chat history, allowing users to interact naturally with the AI assistant in a command-line interface.

---

## 🎯 Project Objectives

* Build a fully local AI-powered chatbot.
* Integrate an open-source Large Language Model (LLM).
* Maintain conversational context across interactions.
* Explore LangChain's prompt engineering and memory capabilities.
* Create a lightweight and privacy-focused conversational AI application.

---

## 🛠 Technologies Used

### Programming Language

* Python

### AI & LLM Frameworks

* LangChain
* Ollama

### Language Model

* TinyLlama

### Environment

* Local Machine
* Command Line Interface (CLI)

---

## 🏗 System Architecture

```text
User Input
     │
     ▼
LangChain Prompt Template
     │
     ▼
Conversation History
     │
     ▼
TinyLlama (via Ollama)
     │
     ▼
AI Response
     │
     ▼
Chat History Update
```

---

## ⚙️ Key Features

### 🧠 Conversational Memory

The chatbot stores previous user and AI messages during the session, enabling context-aware responses and more natural conversations.

### 🔒 Privacy-Focused AI

All processing occurs locally through Ollama, ensuring that user conversations are not sent to external servers.

### ⚡ Fast Inference

Using TinyLlama allows efficient execution on consumer hardware while maintaining reasonable response quality.

### 🎯 Prompt Engineering

A structured system prompt guides the model to provide:

* Helpful responses
* Concise answers
* Consistent conversational behavior

### 💻 Interactive CLI Experience

Users can interact continuously until they choose to exit the application.

---

## 📂 Project Structure

```text
Local-AI-Chatbot/
│
├── main.py
├── requirements.txt
├── README.md
│
└── screenshots/
    ├── chatbot_demo.png
    └── conversation_example.png
```

---

## 🔍 How It Works

### Step 1: User Query

The user enters a question through the terminal.

```text
You: What is machine learning?
```

### Step 2: Prompt Construction

LangChain combines:

* System Instructions
* Previous Conversation History
* Current User Query

into a structured prompt.

### Step 3: Model Inference

The prompt is sent to TinyLlama through Ollama for response generation.

### Step 4: Context Retention

Both user messages and AI responses are stored in chat history, enabling context-aware conversations.

---

## 🚀 Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/local-ai-chatbot.git
cd local-ai-chatbot
```

### 2. Install Dependencies

```bash
pip install langchain
pip install langchain-ollama
```

### 3. Install Ollama

Download and install Ollama from:

https://ollama.com

### 4. Pull TinyLlama Model

```bash
ollama pull tinyllama
```

### 5. Run the Application

```bash
python main.py
```

---

## 💬 Example Conversation

```text
Welcome to the AI Chat!

You: What is Artificial Intelligence?

AI: Artificial Intelligence (AI) refers to systems capable of performing tasks that typically require human intelligence, such as reasoning, learning, and decision-making.

You: Give me some applications.

AI: Common applications include chatbots, recommendation systems, healthcare diagnostics, autonomous vehicles, and fraud detection.
```

---

## 📊 Skills Demonstrated

* Python Programming
* Large Language Models (LLMs)
* LangChain Framework
* Ollama Integration
* Prompt Engineering
* Conversational AI
* Context Management
* Local AI Deployment
* Open Source AI Technologies

---

## 🔮 Future Enhancements

* Add persistent memory using a database.
* Develop a Streamlit web interface.
* Support multiple open-source LLMs.
* Integrate Retrieval-Augmented Generation (RAG).
* Enable document-based question answering.
* Add voice input and speech synthesis.

---

## 📈 Learning Outcomes

Through this project, I gained hands-on experience with:

* Running open-source LLMs locally
* Building conversational AI applications
* Designing prompt templates
* Managing chat history and context
* Integrating LangChain with Ollama
* Deploying privacy-focused AI solutions

---

## 📬 Conclusion

This project demonstrates the implementation of a lightweight, locally hosted AI assistant using modern LLM technologies. By combining LangChain, Ollama, and TinyLlama, the application delivers context-aware conversational capabilities while maintaining user privacy and eliminating dependence on external AI APIs.
