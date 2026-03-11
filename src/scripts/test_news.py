from ingest.ingest_news import ingest_news

news = ingest_news()

for n in news[:5]:
    print(n)