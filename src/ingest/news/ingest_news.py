from ingest.news_sources.google_news import fetch_google_news


def ingest_news():

    queries = [
        "fraude bancária",
        "bank fraud",
        "fintech regulation",
        "money laundering"
    ]

    all_news = []

    for q in queries:
        articles = fetch_google_news(q)
        all_news.extend(articles)

    return all_news