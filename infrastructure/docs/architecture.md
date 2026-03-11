# Architecture

This project ships a minimal but functional anti-fraud stack.

## Runtime Flow

1. API ingests transactions
2. Features are enriched (velocity/amount/counterparties/country drift)
3. Scoring generates risk and alerts
4. Data is persisted to the database
5. UI shows alerts, entities, and graph snapshot

## Components

- FastAPI API + WebSocket
- SQLite (default) or Postgres (optional)
- Lightweight static UI served by the API

## Notes

This is intentionally simple. Expand modules under `src/` as needed.