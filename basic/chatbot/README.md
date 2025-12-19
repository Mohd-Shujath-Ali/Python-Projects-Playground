
# 🤖 AI Chatbot using an API

## Overview

Let’s be honest! **interacting with AI models through web dashboards can feel limiting**.
As developers, we prefer tools that are **simple, fast, and live right inside the terminal** 🚀.

This Python script brings an **AI-powered chatbot directly to your command line**.
It uses the **Hugging Face Inference API** to communicate with a hosted language model, allowing you to send prompts and receive intelligent responses in real time.

This project marks a strong progression in my development journey — moving from basic scripts to working with **cloud-hosted AI models**, **secure API authentication**, and **robust error-handling systems** designed for real-world reliability.

---

## ⚡ Features

* Interactive **AI chatbot** running entirely in the terminal.
* Uses **Hugging Face Inference API** for real-time responses.
* Secure API key management using **environment variables**.
* Supports continuous conversation until the user exits.
* Graceful exit using the `quit` command.
* Implements **detailed error handling** for:

  * API response errors
  * Rate limits and authentication failures
  * Network and runtime exceptions
* Organized, readable, and maintainable Python code.
* Designed with production-aware error catalogs.

---

## 🧠 Requirements

### Python Version

* **Python 3.8+**

### Dependencies

The script uses the following external libraries:

| Module            | Purpose                                           | Installation Required   |
| ----------------- | ------------------------------------------------- | ----------------------- |
| `python-dotenv`   | Loads environment variables securely from `.env`. | ✅ Yes                   |
| `requests`        | Handles network and HTTP operations.              | ✅ Yes                   |
| `openai`          | Included for compatibility and future extensions. | ✅ Yes                   |
| `huggingface_hub` | Connects to Hugging Face Inference API.           | ✅ Yes                   |
| `os`              | Accesses environment variables.                   | ❌ No (Standard Library) |

---

### 🧩 Standard Library & Core Concepts Used

| Concept / Function    | Purpose                                    | Used For                              |
| --------------------- | ------------------------------------------ | ------------------------------------- |
| `while True`          | Maintains continuous interaction loop.     | Persistent chat session.              |
| `try / except`        | Handles runtime and API errors gracefully. | Prevents crashes.                     |
| Environment variables | Secures sensitive credentials.             | API key protection.                   |
| Dictionaries          | Stores structured error catalogs.          | Clear error reporting.                |
| Exception inspection  | Identifies error source.                   | Differentiates API vs network errors. |

These come built-in with Python and don’t require installation.

---

## ⚙️ Installation

Install the required dependencies using:

```bash
pip install python-dotenv requests openai huggingface_hub
```

Create a `.env` file in the project directory and add your API key:

```env
API_KEY=your_huggingface_api_key_here
```

---

## 🚀 Usage

Run the chatbot script:

```bash
python main.py
```

Start chatting:

```text
Enter prompt: What is artificial intelligence?
```

Exit the chatbot:

```text
Enter prompt: quit
```


