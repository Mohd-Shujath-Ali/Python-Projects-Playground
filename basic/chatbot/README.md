# 🤖 AI Chatbot using an API

## Overview

As a developer at an early learning stage, I’m starting by building AI interactions directly in the terminal, A simple and focused environment that helps me understand the fundamentals without extra complexity.

This Python project explores how to create an AI-powered chatbot in the command line using the Hugging Face Inference API and the
google/gemma-2-2b-it:nebius model. The goal is to practice working with hosted language models while learning about secure API authentication, structured error handling, and clean program design.

The project is built with extensibility in mind and is planned to evolve into a **web-based chatbot using Flask**.

---

## ⚡ Features

* Interactive **AI chatbot** in the terminal.
* Uses **Hugging Face Inference API** via `InferenceClient`.
* Secure API key management using **environment variables**.
* Continuous conversation loop with clean exit (`quit`).
* Explicit model selection.
* Two-layer **error handling system**:

  * Hugging Face HTTP error catalog
  * Python & network exception catalog
* Clear, readable error messages.
* Designed for real-world reliability and future expansion.

---

## 🧠 Requirements

### Python Version

* **Python 3.8+**

### Dependencies

| Module            | Purpose                                  | Install |
| ----------------- | ---------------------------------------- | ------- |
| `python-dotenv`   | Loads environment variables from `.env`. | ✅ Yes   |
| `requests`        | Handles HTTP and network operations.     | ✅ Yes   |
| `huggingface_hub` | Connects to Hugging Face Inference API.  | ✅ Yes   |
| `openai`          | Reserved for future compatibility.       | ✅ Yes   |
| `os`              | Accesses environment variables.          | ❌ No    |

---

### 🧩 Core Concepts Used

* Environment variables for secure credentials
* Infinite input loop (`while True`)
* Structured dictionaries for error catalogs
* `try / except` for runtime and API failures
* Exception inspection for accurate error reporting

---

## 🧠 Error Handling

The chatbot implements **production-aware error handling** using two catalogs:

* **HF_ERROR_CATALOG**
  Handles API-level errors such as authentication failure, rate limits, and model unavailability.

* **PY_ERROR_CATLOG**
  Handles Python and network-level errors such as connection issues, timeouts, and SSL failures.

This ensures clean failure states and meaningful diagnostics.

---

## ⚙️ Installation

Install dependencies:

```bash
pip install python-dotenv requests openai huggingface_hub
```

Create a `.env` file in the project root:

```env
API_KEY=your_huggingface_api_key_here
```

> ⚠️ Never commit your `.env` file. Add it to `.gitignore`.

---

## 🚀 Usage

Run the chatbot:

```bash
python main.py
```

Start chatting:

```text
Enter prompt: What is artificial intelligence?
```

Exit safely:

```text
Enter prompt: quit
```

---

## 🌐 Future Plans

* Web-based chatbot using **Flask**
* REST API endpoint for AI responses
* Browser-based UI
* Session-based conversations
* Deployment-ready structure

---

## 📌 Notes
.env file is mandatory to run the main.py and add your API_KEY=in it
This project focuses on **clean API integration, defensive programming, and extensibility**, serving as a solid foundation for both CLI and future web-based AI applications.
