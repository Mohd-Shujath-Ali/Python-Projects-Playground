import requests

API_KEY = "d2e4ca5da252486cb63c9283b312613b"
BASE_URL = "https://newsapi.org/v2/everything" #will append parameters to this base url later

def fetch_news(query):
    params = {
        "q": query,
        "from": "2025-10-01",
        "sortBy": "publishedAt",
        "apiKey": API_KEY,
        "language": "en",
        "pageSize": 5  # ( limit to 5 articles but you can change this )
    }

    print("\nFetching news articles...")
    try:
        response = requests.get(BASE_URL, params=params, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching news: {e}")
        return []

    data = response.json()
    return data.get("articles", [])

def display_articles(articles):
    if not articles:
        print("No articles found for the given query.")
        return

    for i, article in enumerate(articles, start=1):
        print(f"\nArticle {i}:")
        print(f"Title: {article.get('title')}")
        print(f"Description: {article.get('description')}")
        print(f"URL: {article.get('url')}")

if __name__ == "__main__":
    query = input("Enter your search query: ").strip()
    articles = fetch_news(query)
    display_articles(articles)
