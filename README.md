<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0a0000,40:8B0000,80:DC143C,100:ff4444&height=220&section=header&text=FRAUD%20MASTER%20BANK&fontSize=62&fontColor=ffffff&animation=fadeIn&fontAlignY=44&desc=Real-Time%20Fraud%20Intelligence%20%E2%80%B7%20Explainable%20Risk%20Scoring%20%E2%80%B7%20Production-Ready&descAlignY=66&descSize=16&descColor=ffcccc" width="100%" alt="Fraud Master Bank"/>

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=700&size=15&duration=2600&pause=800&color=FF3B3B&center=true&vCenter=true&multiline=false&width=520&lines=Real-Time+Transaction+Fraud+Detection+%F0%9F%94%B4;End-to-End+Operational+Pipeline+%E2%9C%85;Explainable+Risk+Scoring+Engine+%E2%9A%A1;WebSocket+Live+Alerts+%C2%B7+FastAPI+%C2%B7+PostgreSQL;Zero+Black+Boxes.+Zero+Simulated+Data." alt="Typing SVG"/>

<br/><br/>

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.111+-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Production-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)](https://postgresql.org)
[![SQLite](https://img.shields.io/badge/SQLite-Zero%20Config-003B57?style=for-the-badge&logo=sqlite&logoColor=white)](https://sqlite.org)
[![WebSocket](https://img.shields.io/badge/WebSocket-Live%20Alerts-E34F26?style=for-the-badge&logoColor=white)](https://developer.mozilla.org/docs/Web/API/WebSockets_API)
[![Status](https://img.shields.io/badge/Status-Operational-00C9A7?style=for-the-badge&logo=checkmarx&logoColor=white)](.)
[![License](https://img.shields.io/badge/License-Proprietary-DC143C?style=for-the-badge&logo=opensourceinitiative&logoColor=white)](LICENSE)
[![Architecture](https://img.shields.io/badge/Architecture-Event--Driven-6A0DAD?style=for-the-badge&logo=apachekafka&logoColor=white)](.)

<br/>

**A fully operational, production-grade banking fraud detection platform** — real-time transaction ingestion,<br/>
behavioral feature enrichment, fully auditable risk scoring, and live WebSocket alerting.<br/>
Every step is persisted, traceable, and built to extend.

<br/>

> No black boxes. No synthetic data. No toy pipelines.<br/>
> **This is a real system — built to run, extend, and deploy.**

</div>

---

## 📋 Table of Contents

- [What is Fraud Master Bank?](#-what-is-fraud-master-bank)
- [System Architecture](#-system-architecture)
- [Data Flow](#-data-flow)
- [Quick Start](#-quick-start)
- [Persistence & Database Backends](#-persistence--database-backends)
- [API Reference](#-api-reference)
- [Transaction Ingestion](#-transaction-ingestion)
- [Risk Scoring Engine](#-risk-scoring-engine)
- [Project Structure](#-project-structure)
- [Data Reset & Cleanup](#-data-reset--cleanup)
- [Troubleshooting](#-troubleshooting)
- [Roadmap](#-roadmap)
- [Contributing](#-contributing)

---

## ⚡ What is Fraud Master Bank?

**Fraud Master Bank** is a complete, production-ready anti-fraud intelligence platform built on **FastAPI**, featuring dual database support (SQLite / PostgreSQL), real-time WebSocket streaming, and a fully transparent, rule-driven scoring engine.

Every transaction ingested runs through a complete, uninterrupted pipeline:

```
  INGEST  ──▶  ENRICH  ──▶  SCORE  ──▶  ALERT  ──▶  DASHBOARD
```

Nothing is mocked. Everything is persisted, traceable, and extensible — from the first byte to the final flag.

---

## 🧠 System Architecture

```
╔══════════════════════════════════════════════════════════════════════════════╗
║                           FRAUD MASTER BANK                                  ║
║                      Enterprise Anti-Fraud Platform                          ║
╠══════════════════════════════════════════════════════════════════════════════╣
║                                                                               ║
║   ┌─────────────────┐    ┌──────────────────────┐    ┌────────────────────┐ ║
║   │   REST API      │───▶│   INGESTION          │───▶│  ENRICHMENT        │ ║
║   │ POST /ingest    │    │   Pipeline           │    │  · Velocity (24h)  │ ║
║   └─────────────────┘    └──────────────────────┘    │  · Total volume    │ ║
║                                                        │  · Counterparties  │ ║
║   ┌─────────────────┐                                 │  · Geo deviation   │ ║
║   │  Web UI Form    │────────────────────────────────▶└────────┬───────────┘ ║
║   └─────────────────┘                                          ▼             ║
║                                                  ┌─────────────────────────┐ ║
║                                                  │    RISK SCORING ENGINE  │ ║
║                                                  │   Explainable · Audited │ ║
║                                                  └────────┬────────────────┘ ║
║                              ┌─────────────────────────────┤                 ║
║                              ▼                             ▼                 ║
║            ┌──────────────────────────┐    ┌──────────────────────────────┐ ║
║            │    DATABASE LAYER        │    │   WEBSOCKET STREAM           │ ║
║            │  SQLite  ·  PostgreSQL   │    │   /ws/alerts  ·  Live Push   │ ║
║            └──────────────────────────┘    └──────────────────────────────┘ ║
║                            ▼                                                 ║
║            ┌──────────────────────────┐                                     ║
║            │     WEB DASHBOARD        │                                     ║
║            │   http://localhost:8000  │                                     ║
║            └──────────────────────────┘                                     ║
╚══════════════════════════════════════════════════════════════════════════════╝
```

---

## 🔄 Data Flow

```mermaid
flowchart TD
    A([📥 Transaction Input]) --> B{Ingestion Layer}
    B --> C[Feature Enrichment]
    C --> D1[💰 Amount Signal]
    C --> D2[🌍 Geography Signal]
    C --> D3[⚡ Velocity Signal]
    C --> D4[👥 Counterparty Signal]
    C --> D5[⚠️ Channel Signal]
    D1 & D2 & D3 & D4 & D5 --> E[🧠 Risk Scoring Engine]
    E --> F{Score Threshold}
    F -- Score ≥ 0.7 --> G[🔴 HIGH RISK ALERT]
    F -- Score 0.4–0.69 --> H[🟡 MEDIUM RISK]
    F -- Score < 0.4 --> I[🟢 LOW RISK]
    G --> J[(Database)]
    H --> J
    I --> J
    G --> K[📡 WebSocket Push]
    K --> L([🖥️ Live Dashboard])
    J --> L
```

---

## 🚀 Quick Start

### 1 — Clone & create virtual environment

```bash
git clone https://github.com/your-org/fraud-master-bank.git
cd fraud-master-bank
python -m venv .venv
```

### 2 — Activate, install & launch

| 🪟 Windows · PowerShell | 🍎 macOS · 🐧 Linux |
|:---|:---|
| `.venv\Scripts\Activate.ps1` | `source .venv/bin/activate` |
| `pip install -r requirements.txt` | `pip install -r requirements.txt` |
| `uvicorn src.Backend.app:app --reload` | `uvicorn src.Backend.app:app --reload` |

### 3 — Open in your browser

| Interface | Address |
|:---|:---|
| 🖥️ **Dashboard** | `http://127.0.0.1:8000` |
| 📡 **REST API** | `http://127.0.0.1:8000/api/v1` |
| 🔴 **WebSocket — Live Alerts** | `ws://127.0.0.1:8000/ws/alerts` |
| 📖 **Swagger Docs** | `http://127.0.0.1:8000/docs` |

---

## 💾 Persistence & Database Backends

The platform ships with **SQLite enabled by default** — zero configuration, zero setup. The schema is auto-provisioned on first boot. Switch to PostgreSQL for production workloads in three steps.

```
╔════════════════════════════════════════════════════════════════════════════╗
║                        DATABASE BACKENDS                                    ║
╠══════════════════════════════════════╦═════════════════════════════════════╣
║  SQLite  ·  Default                  ║  PostgreSQL  ·  Production           ║
╠══════════════════════════════════════╬═════════════════════════════════════╣
║  ✅  Zero configuration              ║  🔧  Requires .env setup             ║
║  ✅  File-based · portable           ║  ✅  Production-ready                 ║
║  ✅  Instant demos & local dev       ║  ✅  Concurrent connections           ║
║  ✅  Auto schema provisioning        ║  ✅  Remote & cloud databases         ║
╚══════════════════════════════════════╩═════════════════════════════════════╝
```

### Migrating to PostgreSQL

```bash
# Step 1 — copy the environment template
cp .env.example .env

# Step 2 — configure your connection string in .env
DATABASE_URL=postgresql://user:password@host:5432/database_name

# Step 3 — restart · schema migrates automatically
uvicorn src.Backend.app:app --reload
```

---

## 📡 API Reference

| Method | Endpoint | Description |
|:---:|:---|:---|
| `GET` | `/health` | Application health check |
| `POST` | `/api/v1/transactions/ingest` | Ingest one or more transactions |
| `GET` | `/api/v1/transactions` | List all transactions |
| `GET` | `/api/v1/alerts` | List all fraud alerts |
| `GET` | `/api/v1/entities` | List all tracked entities |
| `GET` | `/api/v1/graph` | Entity relationship graph |
| `GET` | `/api/v1/investigations` | List open investigations |
| `POST` | `/api/v1/investigations` | Open a new investigation |
| `PATCH` | `/api/v1/investigations/{id}` | Update investigation status |
| `WS` | `/ws/alerts` | Real-time alert stream |

---

## 🔌 Transaction Ingestion

Submit a JSON array to the ingestion endpoint. The pipeline will **enrich behavioral features**, **compute a risk score**, **persist to the database**, and **push WebSocket alerts** — all within a single request.

**Transaction schema:**

```jsonc
{
  "entity_id":       "account_001",  // Source account ID
  "counterparty_id": "account_002",  // Destination account ID
  "amount":          15000,          // Transaction amount (numeric)
  "currency":        "USD",          // ISO 4217 currency code
  "channel":         "atm",          // atm | wire | crypto | online | branch
  "country":         "US"            // ISO 3166-1 alpha-2 country code
}
```

**🪟 PowerShell:**

```powershell
curl -X POST http://127.0.0.1:8000/api/v1/transactions/ingest `
  -H "Content-Type: application/json" `
  -d "[{`"entity_id`":`"acc_1`",`"counterparty_id`":`"acc_2`",`"amount`":15000,`"currency`":`"USD`",`"channel`":`"atm`",`"country`":`"US`"}]"
```

**🍎 macOS / 🐧 Linux:**

```bash
curl -X POST http://127.0.0.1:8000/api/v1/transactions/ingest \
  -H "Content-Type: application/json" \
  -d '[{"entity_id":"acc_1","counterparty_id":"acc_2","amount":15000,"currency":"USD","channel":"atm","country":"US"}]'
```

---

## 🔴 Risk Scoring Engine

The scoring engine (`src/intelligence/risk_engine/scoring_model.py`) is a **transparent, rule-based model** designed for maximum auditability. Every score can be traced back to its individual contributing signals — no guesswork, no opacity.

```
╔══════════════════════════════════════════════════════════════════════════════╗
║                           RISK SIGNAL MATRIX                                 ║
╠══════════════════════════════╦═══════════════════════════════════════════════╣
║  💰  Amount                  ║  Transactions exceeding high-value threshold  ║
║  🌍  Geography               ║  Cross-border and international transfers     ║
║  ⚡  Velocity                ║  Transaction count in the last 24 hours       ║
║  📦  Volume                  ║  Total value moved in the last 24 hours       ║
║  👥  Counterparties          ║  Distinct destination accounts in 24h         ║
║  🗺️  Geographic Drift        ║  Country shift vs. recent behavioral history  ║
║  ⚠️  High-Risk Channel       ║  Critical channels: ATM · Crypto              ║
╚══════════════════════════════╩═══════════════════════════════════════════════╝
```

```
Risk Score   0.0 ════════════════════════════════════════════════════ 1.0
                  ║    LOW RISK     ║   MEDIUM RISK   ║  HIGH RISK  ║
                  ╚═════════════════╩═════════════════╩═════════════╝
                                                              ▲
                                                    ┌─────────┴────────┐
                                                    │  ALERT TRIGGERED │
                                                    │  → WebSocket push│
                                                    │  → DB persisted  │
                                                    │  → UI flagged    │
                                                    └──────────────────┘
```

> Extend the engine at `src/intelligence/risk_engine/scoring_model.py` — plug in ML models, graph centrality features, or external watchlists without touching any other part of the pipeline.

---

## 📁 Project Structure

```
fraud-master-bank/
│
├── 📁 src/
│   ├── 📁 Backend/
│   │   ├── 🐍 app.py                ◀  FastAPI application · routes & middleware
│   │   ├── 🐍 schemas.py            ◀  Pydantic models · request / response
│   │   ├── 📁 services/             ◀  Business logic layer
│   │   └── 📁 static/              ◀  Web dashboard (HTML · CSS · JS)
│   │
│   ├── 📁 pipelines/               ◀  Ingestion & processing pipelines
│   │
│   ├── 📁 intelligence/
│   │   └── 📁 risk_engine/
│   │       └── 🐍 scoring_model.py  ◀  ⭐ Core scoring logic
│   │
│   └── 📁 db/                      ◀  ORM models · sessions · migrations
│
├── 📁 data/
│   └── 🗄️ fraud_master_bank.db     ◀  SQLite database (auto-created)
│
├── 📄 .env.example
├── 📄 requirements.txt
└── 📄 README.md
```

---

## 🧹 Data Reset & Cleanup

| 🪟 PowerShell | 🍎 macOS · 🐧 Linux |
|:---|:---|
| `Remove-Item -Force .\data\fraud_master_bank.db -ErrorAction SilentlyContinue` | `rm -f ./data/fraud_master_bank.db` |

Restart the server — the schema will be recreated automatically.

---

## 🛠️ Troubleshooting

<details>
<summary><strong>🔇 &nbsp; Dashboard loads but shows no data</strong></summary>
<br/>
The dashboard requires at least one ingested transaction to display metrics. Submit one via the UI form or call <code>/api/v1/transactions/ingest</code> directly using <code>curl</code> or the Swagger UI at <code>/docs</code>.
</details>

<details>
<summary><strong>🔌 &nbsp; WebSocket shows "Disconnected"</strong></summary>
<br/>
Make sure the server is running and you are accessing it at exactly <code>http://127.0.0.1:8000</code>. WebSocket connections will fail on any host or port mismatch.
</details>

<details>
<summary><strong>🐘 &nbsp; PostgreSQL connection errors</strong></summary>
<br/>

1. Confirm the database server is reachable.
2. Verify `DATABASE_URL` in your `.env`:
```dotenv
DATABASE_URL=postgresql://user:password@host:5432/database_name
```
3. Ensure the target database exists before starting the application.
4. Check firewall rules and `pg_hba.conf` for remote connections.
</details>

<details>
<summary><strong>📦 &nbsp; Dependency installation failure</strong></summary>
<br/>

```bash
pip install --upgrade pip
pip install -r requirements.txt
```
</details>

---

## 🗺️ Roadmap

| Status | Feature |
|:---:|:---|
| ✅ | Transaction ingestion pipeline |
| ✅ | Rule-based explainable scoring engine |
| ✅ | Real-time WebSocket alerting |
| ✅ | SQLite + PostgreSQL dual persistence |
| ✅ | Investigation management API |
| ✅ | Entity relationship graph API |
| 🔄 | ML scoring model (XGBoost · Isolation Forest) |
| 🔄 | Graph neural network for counterparty ring detection |
| 📋 | External watchlist integration (OFAC · PEP · FATF) |
| 📋 | Case management dashboard |
| 📋 | SAR (Suspicious Activity Report) export |
| 📋 | Multi-tenant support |
| 📋 | Kafka / Kinesis streaming ingestion |
| 📋 | GDPR-compliant data anonymization layer |

---

## 🤝 Contributing

Contributions are welcome across these areas:

- **New scoring signals** — velocity refinements, graph centrality, behavioral baselines
- **ML model integration** — trained classifiers wired into the scoring pipeline
- **Data connectors** — batch CSV ingestion, Kafka consumers, inbound webhooks
- **Infrastructure** — Docker Compose, Kubernetes manifests, CI/CD pipelines
- **Testing** — unit tests for scoring logic, integration tests for the full API surface

---

<div align="center">

<br/>

*Built to detect. Designed to explain. Architected to scale.*

<br/>

[![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=flat-square&logo=postgresql&logoColor=white)](https://postgresql.org)
[![SQLite](https://img.shields.io/badge/SQLite-003B57?style=flat-square&logo=sqlite&logoColor=white)](https://sqlite.org)
[![WebSocket](https://img.shields.io/badge/WebSocket-E34F26?style=flat-square&logoColor=white)](https://developer.mozilla.org/docs/Web/API/WebSockets_API)
[![XGBoost](https://img.shields.io/badge/XGBoost-Coming%20Soon-FF6600?style=flat-square&logo=xgboost&logoColor=white)](.)
[![OFAC](https://img.shields.io/badge/OFAC%20Watchlist-Roadmap-6A0DAD?style=flat-square&logoColor=white)](.)

<br/>

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0a0000,40:8B0000,80:DC143C,100:ff4444&height=130&section=footer&text=Fraud%20Master%20Bank%20%C2%B7%20Real-Time%20Financial%20Intelligence&fontSize=14&fontColor=ffcccc&fontAlignY=66&animation=fadeIn" width="100%" alt="footer"/>

</div>
