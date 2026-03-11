import feedparser


def fetch_google_news(query="fraude bancária", limit=20):

    url = f"https://news.google.com/rss/search?q={query}"

    feed = feedparser.parse(url)

    articles = []

    for entry in feed.entries[:limit]:

        articles.append({
            "title": entry.title,
            "link": entry.link,
            "published_at": entry.published,
            "source": "Google News"
        })

    return articles