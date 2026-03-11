from ingest.ingest_news import ingest_news
from db.db import get_db


def run_news_pipeline():

    db = get_db()

    news = ingest_news()

    for article in news:

        db.execute(
            """
            INSERT INTO news (title, source, url, published_at)
            VALUES (:title, :source, :url, :published_at)
            """,
            {
                "title": article["title"],
                "source": article["source"],
                "url": article["link"],
                "published_at": article["published_at"]
            }
        )

    db.commit()