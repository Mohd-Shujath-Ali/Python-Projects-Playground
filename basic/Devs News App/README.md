# 📰 News Fetcher Script

## Overview

Let’s be honest!  **searching for news manually on a browser is boring**.  
As developers, we prefer to keep things efficient, automated, and just a bit geeky 😎.  

So, this Python script brings the **world’s latest headlines straight to your terminal**.  
It uses the [NewsAPI](https://newsapi.org/) to fetch articles based on your search query and displays the **top 5 latest results** with their **titles**, **descriptions**, and **URLs** — which you can open directly in your browser if something catches your eye.

This project marks a level-up in my Python journey — from writing basic local scripts to integrating **real-world APIs**, handling **JSON data**, and applying **clean modular code**.

---

## ⚡ Features

- Fetches **real-time news** on any topic using your search query.
- Displays each article’s **title**, **description**, and **URL**.
- Lets developers read and explore news **directly from the terminal** — no browser needed.
- Uses **parameterized API calls** for safety and clarity.
- Includes **robust error handling** with `try/except`.
- Organized into **modular functions** for clean, reusable code.
- Follows core Python best practices like `enumerate()` and `if __name__ == "__main__"`.

---

## 🧠 Requirements

### Python Version
- **Python 3.7+**

### Dependencies

The script requires just **one external library**:

| Module | Purpose | Installation Required |
|---------|----------|------------------------|
| `requests` | Handles HTTP requests to fetch data from NewsAPI. | ✅ Yes |

---

### 🧩 Standard Library Concepts Used

| Concept / Function | Purpose | Used For |
|---------------------|----------|----------|
| `try / except` | Handles runtime errors gracefully. | Prevents crashes due to network or API issues. |
| `enumerate()` | Adds automatic numbering during loops. | Numbers the displayed news articles. |
| `if __name__ == "__main__":` | Defines the script’s entry point. | Ensures clean execution and reusability. |
| **Functions (`def`)** | Makes code organized and modular. | Separates logic into `fetch_news()` and `display_articles()`. |

These come built-in with Python and don’t require installation.

---

## ⚙️ Installation

Install the required module using:

```bash
pip install requests
