<div align="center">

```
███████╗██████╗  █████╗ ██╗   ██╗██████╗
██╔════╝██╔══██╗██╔══██╗██║   ██║██╔══██╗
█████╗  ██████╔╝███████║██║   ██║██║  ██║
██╔══╝  ██╔══██╗██╔══██║██║   ██║██║  ██║
██║     ██║  ██║██║  ██║╚██████╔╝██████╔╝
╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═════╝

███╗   ███╗ █████╗ ███████╗████████╗███████╗██████╗
████╗ ████║██╔══██╗██╔════╝╚══██╔══╝██╔════╝██╔══██╗
██╔████╔██║███████║███████╗   ██║   █████╗  ██████╔╝
██║╚██╔╝██║██╔══██║╚════██║   ██║   ██╔══╝  ██╔══██╗
██║ ╚═╝ ██║██║  ██║███████║   ██║   ███████╗██║  ██║
╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝

██████╗  █████╗ ███╗   ██╗██╗  ██╗
██╔══██╗██╔══██╗████╗  ██║██║ ██╔╝
██████╔╝███████║██╔██╗ ██║█████╔╝
██╔══██╗██╔══██║██║╚██╗██║██╔═██╗
██████╔╝██║  ██║██║ ╚████║██║  ██╗
╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝
```

**Operational · End-to-End · Anti-Fraud Intelligence**

---

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.111-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![SQLite](https://img.shields.io/badge/SQLite-Default%20DB-003B57?style=for-the-badge&logo=sqlite&logoColor=white)](https://www.sqlite.org/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Optional-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![WebSocket](https://img.shields.io/badge/WebSocket-Real--Time%20Alerts-E34F26?style=for-the-badge&logo=websocket&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API)
[![License](https://img.shields.io/badge/License-Proprietary-DC143C?style=for-the-badge)](LICENSE)

</div>

---

## ⚡ What is Fraud Master Bank?

> A **production-grade, fully operational anti-fraud demo platform** built on FastAPI — capable of ingesting financial transactions in real time, enriching them with behavioral features, scoring risk with an explainable rule-based engine, and surfacing alerts through a live WebSocket-powered dashboard.

No black boxes. No mock data. No toy pipelines. This is a **real end-to-end system** you can run, extend, and deploy.

---

## 🧠 System Overview

```
                        ┌─────────────────────────────────────────────────┐
                        │               FRAUD MASTER BANK                  │
                        │                                                   │
  ┌──────────────┐      │   ┌─────────────┐      ┌──────────────────────┐ │
  │   REST API   │─────▶│   │  INGESTION  │─────▶│   FEATURE ENRICHMENT │ │
  │ POST /ingest │      │   │  Pipeline   │      │  · Velocity (24h)    │ │
  └──────────────┘      │   └─────────────┘      │  · Volume            │ │
                        │          │              │  · Counterparty count│ │
  ┌──────────────┐      │          ▼              │  · Country drift     │ │
  │  Web UI Form │─────▶│   ┌─────────────┐      └──────────┬───────────┘ │
  └──────────────┘      │   │  RISK ENGINE│◀─────────────────┘           │ │
                        │   │  Scoring    │                               │ │
                        │   └──────┬──────┘                               │ │
                        │          │                                       │ │
                        │    ┌─────▼──────┐     ┌──────────────────────┐ │ │
                        │    │   ALERTS   │────▶│   WebSocket Stream   │ │ │
                        │    └──────┬─────┘     │   /ws/alerts         │ │ │
                        │           │            └──────────────────────┘ │ │
                        │    ┌──────▼─────┐                               │ │
                        │    │  DATABASE  │     ┌──────────────────────┐ │ │
                        │    │  SQLite /  │────▶│   Dashboard UI       │ │ │
                        │    │  Postgres  │     │   http://localhost   │ │ │
                        │    └────────────┘     └──────────────────────┘ │ │
                        └─────────────────────────────────────────────────┘
```

---

## 🚀 Quickstart

### 1 · Clone & Create Virtual Environment

```bash
git clone https://github.com/your-org/fraud-master-bank.git
cd fraud-master-bank
python -m venv .venv
```

### 2 · Activate & Install

<table>
<tr>
<th>🪟 Windows (PowerShell)</th>
<th>🍎 macOS / 🐧 Linux</th>
</tr>
<tr>
<td>

```powershell
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn src.Backend.app:app --reload
```

</td>
<td>

```bash
source .venv/bin/activate
pip install -r requirements.txt
uvicorn src.Backend.app:app --reload
```

</td>
</tr>
</table>

### 3 · Open in Browser

| Interface | URL |
|---|---|
| 🖥️ **Dashboard UI** | [http://127.0.0.1:8000](http://127.0.0.1:8000) |
| 📡 **REST API** | [http://127.0.0.1:8000/api/v1](http://127.0.0.1:8000/api/v1) |
| 🔴 **WebSocket Alerts** | `ws://127.0.0.1:8000/ws/alerts` |
| 📖 **Swagger Docs** | [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) |

---

## 💾 Persistence & Database

Fraud Master Bank supports two database backends. SQLite works out of the box — no configuration required. The schema is created automatically on startup.

```
┌─────────────────────────────────────────────────────────┐
│                    DATABASE BACKENDS                     │
├────────────────────────┬────────────────────────────────┤
│  SQLite (default)      │  PostgreSQL (production)       │
├────────────────────────┼────────────────────────────────┤
│  ✅ Zero config        │  🔧 Requires .env setup        │
│  ✅ File-based         │  ✅ Production-grade           │
│  ✅ Great for demos    │  ✅ Concurrent connections     │
│  📁 ./data/fraud_      │  🌐 Remote/cloud DBs          │
│     master_bank.db     │                                │
└────────────────────────┴────────────────────────────────┘
```

### Switching to PostgreSQL

**Step 1** — Copy the example env file:

```bash
cp .env.example .env
```

**Step 2** — Edit `.env` and set your connection string:

```dotenv
DATABASE_URL=postgresql://user:password@host:5432/dbname
```

**Step 3** — Restart the server. Schema migration runs automatically.

---

## 📡 API Reference

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/health` | Health check |
| `POST` | `/api/v1/transactions/ingest` | Ingest one or more transactions |
| `GET` | `/api/v1/transactions` | List all transactions |
| `GET` | `/api/v1/alerts` | List all fraud alerts |
| `GET` | `/api/v1/entities` | List all entities |
| `GET` | `/api/v1/graph` | Graph relationships between entities |
| `GET` | `/api/v1/investigations` | List investigations |
| `POST` | `/api/v1/investigations` | Create a new investigation |
| `PATCH` | `/api/v1/investigations/{id}` | Update investigation status |
| `WS` | `/ws/alerts` | Real-time WebSocket alert stream |

---

## 🔌 Ingesting Transactions

Send a JSON array of transaction objects to the ingest endpoint. The pipeline will enrich features, score risk, persist to DB, and push alerts via WebSocket — all in a single request.

**Transaction Schema:**

```json
{
  "entity_id":       "acct_001",       // sender account ID
  "counterparty_id": "acct_002",       // receiver account ID
  "amount":          15000,            // transaction amount (numeric)
  "currency":        "USD",            // ISO 4217 currency code
  "channel":         "atm",            // atm | wire | crypto | online | branch
  "country":         "US"             // ISO 3166-1 alpha-2 country code
}
```

**Send a transaction:**

<table>
<tr>
<th>🪟 PowerShell</th>
</tr>
<tr>
<td>

```powershell
curl -X POST http://127.0.0.1:8000/api/v1/transactions/ingest `
  -H "Content-Type: application/json" `
  -d "[{`"entity_id`":`"acct_1`",`"counterparty_id`":`"acct_2`",`"amount`":15000,`"currency`":`"USD`",`"channel`":`"atm`",`"country`":`"US`"}]"
```

</td>
</tr>
<tr>
<th>🍎 macOS / 🐧 Linux</th>
</tr>
<tr>
<td>

```bash
curl -X POST http://127.0.0.1:8000/api/v1/transactions/ingest \
  -H "Content-Type: application/json" \
  -d '[{"entity_id":"acct_1","counterparty_id":"acct_2","amount":15000,"currency":"USD","channel":"atm","country":"US"}]'
```

</td>
</tr>
</table>

---

## 🔴 Risk Scoring Engine

The scoring engine (`src/intelligence/risk_engine/scoring_model.py`) is a **transparent, rule-based model** designed for auditability and explainability. Every score can be traced back to its contributing signals.

```
┌──────────────────────────────────────────────────────────────────────────┐
│                        RISK SCORING SIGNALS                               │
├──────────────────┬───────────────────────────────────────────────────────┤
│  SIGNAL          │  DESCRIPTION                                          │
├──────────────────┼───────────────────────────────────────────────────────┤
│  💰 Amount       │  High-value transactions above threshold              │
│  🌍 Geography    │  International transfers, cross-border activity        │
│  ⚡ Velocity     │  Transaction count in the last 24 hours               │
│  📦 Volume       │  Total amount moved in the last 24 hours              │
│  👥 Counterparty │  Number of distinct counterparties in 24h             │
│  🗺️ Country Drift│  Country change vs recent transaction history         │
│  ⚠️ Channel Risk │  High-risk channels: ATM, Crypto                      │
└──────────────────┴───────────────────────────────────────────────────────┘

                         Risk Score → Alert Generation

    Score 0.0 ────────────────────────────────────────────── 1.0
              │ LOW RISK │    MEDIUM RISK   │   HIGH RISK   │
              └──────────┴──────────────────┴───────────────┘
                                                   ▲
                                             ALERT CREATED
                                          → WebSocket push
                                          → DB persisted
                                          → Dashboard flagged
```

> Extend the scoring model at `src/intelligence/risk_engine/scoring_model.py` — add ML models, graph-based features, or external watchlist lookups without touching the rest of the pipeline.

---

## 📁 Project Structure

```
fraud-master-bank/
│
├── 📁 src/
│   ├── 📁 Backend/
│   │   ├── 🐍 app.py                  # FastAPI application & route definitions
│   │   ├── 🐍 schemas.py              # Pydantic request/response models
│   │   ├── 📁 services/               # Business logic layer
│   │   └── 📁 static/                 # Dashboard UI (HTML/CSS/JS)
│   │
│   ├── 📁 pipelines/                  # Data ingestion & processing pipelines
│   │
│   ├── 📁 intelligence/
│   │   └── 📁 risk_engine/
│   │       └── 🐍 scoring_model.py    # ⭐ Core fraud scoring logic
│   │
│   └── 📁 db/                         # Database models, sessions, migrations
│
├── 📁 data/
│   └── 🗄️ fraud_master_bank.db        # SQLite database (auto-created)
│
├── 📄 .env.example                    # Environment variable template
├── 📄 requirements.txt                # Python dependencies
└── 📄 README.md
```

---

## 🧹 Reset & Cleanup

To wipe all data and start fresh:

<table>
<tr>
<th>🪟 PowerShell</th>
<th>🍎 macOS / 🐧 Linux</th>
</tr>
<tr>
<td>

```powershell
Remove-Item -Force .\data\fraud_master_bank.db `
  -ErrorAction SilentlyContinue
```

</td>
<td>

```bash
rm -f ./data/fraud_master_bank.db
```

</td>
</tr>
</table>

Restart the server — the schema will be recreated automatically.

---

## 🛠️ Troubleshooting

<details>
<summary><strong>🔇 UI loads but shows no data</strong></summary>

The dashboard requires at least one transaction to display data. Ingest a transaction using the UI form or by calling `/api/v1/transactions/ingest` directly via `curl` or the Swagger UI at `/docs`.

</details>

<details>
<summary><strong>🔌 WebSocket shows "Disconnected"</strong></summary>

Ensure the API server is running (`uvicorn ... --reload`) and that you are accessing the app at exactly `http://127.0.0.1:8000`. WebSocket connections will fail if there is a host or port mismatch between the page origin and the WS endpoint.

</details>

<details>
<summary><strong>🐘 PostgreSQL connection errors</strong></summary>

1. Confirm the database server is reachable from your machine.
2. Verify the `DATABASE_URL` in your `.env` file is correct:
   ```
   DATABASE_URL=postgresql://user:password@host:5432/dbname
   ```
3. Ensure the target database exists before starting the app.
4. Check firewall rules and pg_hba.conf if connecting remotely.

</details>

<details>
<summary><strong>📦 Dependency installation fails</strong></summary>

Make sure you have Python 3.10+ and that the virtual environment is activated before running `pip install`. On some systems you may need to upgrade pip first:

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

</details>

---

## 🗺️ Roadmap

| Status | Feature |
|---|---|
| ✅ Done | Transaction ingestion pipeline |
| ✅ Done | Rule-based risk scoring engine |
| ✅ Done | Real-time WebSocket alerts |
| ✅ Done | SQLite + PostgreSQL persistence |
| ✅ Done | Investigation management API |
| ✅ Done | Entity graph API |
| 🔄 In Progress | ML-based scoring model (XGBoost / Isolation Forest) |
| 🔄 In Progress | Graph neural network for counterparty rings |
| 📋 Planned | External watchlist integration (OFAC, PEP lists) |
| 📋 Planned | Case management dashboard |
| 📋 Planned | SAR (Suspicious Activity Report) export |
| 📋 Planned | Multi-tenant support |
| 📋 Planned | Kafka / Kinesis streaming ingest |

---

## 🤝 Contributing

Contributions are welcome in the following areas:

- **New scoring signals** — velocity patterns, graph centrality, behavioral baselines
- **ML model integration** — plug in trained classifiers into the scoring pipeline
- **Data connectors** — new ingest formats (CSV bulk, Kafka, webhook)
- **Infrastructure** — Docker Compose setup, Kubernetes manifests, CI/CD pipelines
- **Testing** — unit tests for scoring logic, integration tests for the API

---

<div align="center">

---

**Fraud Master Bank** · Anti-Fraud Intelligence Platform

*Built to detect. Engineered to explain. Designed to scale.*

</div>