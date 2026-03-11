<div align="center">

<!-- BANNER — renderiza no GitHub desktop e mobile como imagem -->
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:8B0000,60:DC143C,100:1a0000&height=200&section=header&text=FRAUD%20MASTER%20BANK&fontSize=56&fontColor=ffffff&animation=fadeIn&fontAlignY=42&desc=Intelig%C3%AAncia%20Antifraude%20%E2%80%B7%20Tempo%20Real%20%E2%80%B7%20Produ%C3%A7%C3%A3o&descAlignY=64&descSize=17&descColor=ffcccc" width="100%" alt="Fraud Master Bank"/>

<!-- TYPING ANIMATION -->
<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=700&size=16&duration=2800&pause=900&color=DC143C&center=true&vCenter=true&width=480&lines=Detec%C3%A7%C3%A3o+de+Fraudes+em+Tempo+Real+%F0%9F%94%B4;Pipeline+Operacional+End-to-End;Scoring+de+Risco+Explic%C3%A1vel+%E2%9A%A1;WebSocket+%C2%B7+FastAPI+%C2%B7+PostgreSQL" alt="Typing"/>

<br/><br/>

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.111+-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![SQLite](https://img.shields.io/badge/SQLite-Padrão-003B57?style=for-the-badge&logo=sqlite&logoColor=white)](https://sqlite.org)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Opcional-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)](https://postgresql.org)
[![WebSocket](https://img.shields.io/badge/WebSocket-Alertas%20ao%20Vivo-E34F26?style=for-the-badge&logoColor=white)](https://developer.mozilla.org/docs/Web/API/WebSockets_API)
[![Status](https://img.shields.io/badge/Status-Operacional-00C9A7?style=for-the-badge)](.)
[![Licença](https://img.shields.io/badge/Licença-Proprietária-DC143C?style=for-the-badge)](LICENSE)

<br/>

**Plataforma operacional de detecção de fraudes bancárias** — ingestão de transações em tempo real,<br/>
enriquecimento de features comportamentais, scoring de risco com explicabilidade total<br/>
e alertas ao vivo via WebSocket.

<br/>

> Sem caixas-pretas. Sem dados simulados. Sem pipelines de brinquedo.<br/>
> **Este é um sistema real — pronto para executar, estender e implantar.**

</div>

---

## 📋 Índice

- [O que é o Fraud Master Bank?](#-o-que-é-o-fraud-master-bank)
- [Visão Geral do Sistema](#-visão-geral-do-sistema)
- [Início Rápido](#-início-rápido)
- [Persistência e Banco de Dados](#-persistência-e-banco-de-dados)
- [Referência da API](#-referência-da-api)
- [Ingestão de Transações](#-ingestão-de-transações)
- [Motor de Scoring de Risco](#-motor-de-scoring-de-risco)
- [Estrutura do Projeto](#-estrutura-do-projeto)
- [Reset e Limpeza de Dados](#-reset-e-limpeza-de-dados)
- [Solução de Problemas](#-solução-de-problemas)
- [Roadmap](#-roadmap)
- [Contribuição](#-contribuição)

---

## ⚡ O que é o Fraud Master Bank?

O **Fraud Master Bank** é uma plataforma antifraude completa, operacional e de nível produção — construída sobre **FastAPI** com suporte a banco de dados dual (SQLite / PostgreSQL), WebSocket em tempo real e um motor de scoring totalmente auditável.

Cada transação ingerida passa por um pipeline completo:

```
  INGESTÃO  ──▶  ENRIQUECIMENTO  ──▶  SCORING  ──▶  ALERTA  ──▶  DASHBOARD
```

Nenhuma etapa é simulada. Tudo é persistido, rastreável e extensível.

---

## 🧠 Visão Geral do Sistema

```
╔══════════════════════════════════════════════════════════════════════════╗
║                         FRAUD MASTER BANK                                ║
╠══════════════════════════════════════════════════════════════════════════╣
║                                                                           ║
║   ┌──────────────┐    ┌───────────────────┐    ┌──────────────────────┐ ║
║   │  API REST    │───▶│    INGESTÃO       │───▶│  ENRIQUECIMENTO      │ ║
║   │ POST /ingest │    │    Pipeline       │    │  · Velocidade (24h)  │ ║
║   └──────────────┘    └───────────────────┘    │  · Volume total      │ ║
║                                                 │  · Nº contrapartes   │ ║
║   ┌──────────────┐                             │  · Desvio geográfico │ ║
║   │  Web UI Form │────────────────────────────▶└──────────┬───────────┘ ║
║   └──────────────┘                                        ▼             ║
║                                               ┌──────────────────────┐  ║
║                                               │   MOTOR DE RISCO     │  ║
║                                               │   Scoring Engine     │  ║
║                                               └──────────┬───────────┘  ║
║                                ┌──────────────────────────┤             ║
║                                ▼                          ▼             ║
║              ┌──────────────────────┐      ┌──────────────────────┐    ║
║              │  BANCO DE DADOS      │      │  STREAM WEBSOCKET    │    ║
║              │  SQLite / Postgres   │      │  /ws/alerts          │    ║
║              └──────────┬───────────┘      └──────────────────────┘    ║
║                         ▼                                               ║
║              ┌──────────────────────┐                                  ║
║              │  DASHBOARD WEB       │                                  ║
║              │  http://localhost    │                                  ║
║              └──────────────────────┘                                  ║
╚══════════════════════════════════════════════════════════════════════════╝
```

---

## 🚀 Início Rápido

### 1 — Clone e crie o ambiente virtual

```bash
git clone https://github.com/sua-org/fraud-master-bank.git
cd fraud-master-bank
python -m venv .venv
```

### 2 — Ative e instale as dependências

| 🪟 Windows · PowerShell | 🍎 macOS · 🐧 Linux |
|---|---|
| `.venv\Scripts\Activate.ps1` | `source .venv/bin/activate` |
| `pip install -r requirements.txt` | `pip install -r requirements.txt` |
| `uvicorn src.Backend.app:app --reload` | `uvicorn src.Backend.app:app --reload` |

### 3 — Abra no navegador

| Interface | Endereço |
|:---|:---|
| 🖥️ **Dashboard** | `http://127.0.0.1:8000` |
| 📡 **API REST** | `http://127.0.0.1:8000/api/v1` |
| 🔴 **WebSocket — Alertas** | `ws://127.0.0.1:8000/ws/alerts` |
| 📖 **Swagger Docs** | `http://127.0.0.1:8000/docs` |

---

## 💾 Persistência e Banco de Dados

O sistema suporta dois backends. O **SQLite funciona imediatamente**, sem nenhuma configuração. O schema é criado automaticamente na inicialização.

```
╔══════════════════════════════════════════════════════════════════════╗
║                      BACKENDS DE BANCO DE DADOS                      ║
╠═══════════════════════════════╦══════════════════════════════════════╣
║  SQLite  ·  Padrão            ║  PostgreSQL  ·  Produção             ║
╠═══════════════════════════════╬══════════════════════════════════════╣
║  ✅  Zero configuração        ║  🔧  Requer configuração .env        ║
║  ✅  Baseado em arquivo       ║  ✅  Pronto para produção            ║
║  ✅  Ideal para demos         ║  ✅  Conexões concorrentes           ║
║  ✅  Schema automático        ║  ✅  DBs remotos e em cloud          ║
╚═══════════════════════════════╩══════════════════════════════════════╝
```

### Migrando para PostgreSQL

```bash
# Passo 1 — copie o template
cp .env.example .env

# Passo 2 — configure a conexão no .env
DATABASE_URL=postgresql://usuario:senha@host:5432/nome_do_banco

# Passo 3 — reinicie · o schema migra automaticamente
uvicorn src.Backend.app:app --reload
```

---

## 📡 Referência da API

| Método | Endpoint | Descrição |
|:---:|:---|:---|
| `GET` | `/health` | Verificação de saúde da aplicação |
| `POST` | `/api/v1/transactions/ingest` | Ingerir uma ou mais transações |
| `GET` | `/api/v1/transactions` | Listar todas as transações |
| `GET` | `/api/v1/alerts` | Listar todos os alertas de fraude |
| `GET` | `/api/v1/entities` | Listar todas as entidades |
| `GET` | `/api/v1/graph` | Grafo de relacionamentos entre entidades |
| `GET` | `/api/v1/investigations` | Listar investigações abertas |
| `POST` | `/api/v1/investigations` | Abrir nova investigação |
| `PATCH` | `/api/v1/investigations/{id}` | Atualizar status de investigação |
| `WS` | `/ws/alerts` | Stream de alertas em tempo real |

---

## 🔌 Ingestão de Transações

Envie um array JSON ao endpoint de ingestão. O pipeline irá **enriquecer features**, **calcular o score de risco**, **persistir no banco** e **disparar alertas via WebSocket** — tudo em uma única requisição.

**Schema da transação:**

```jsonc
{
  "entity_id":       "conta_001",  // ID da conta remetente
  "counterparty_id": "conta_002",  // ID da conta destinatária
  "amount":          15000,        // Valor da transação (numérico)
  "currency":        "BRL",        // Código de moeda ISO 4217
  "channel":         "atm",        // atm | wire | crypto | online | agencia
  "country":         "BR"          // Código de país ISO 3166-1 alpha-2
}
```

**🪟 PowerShell:**

```powershell
curl -X POST http://127.0.0.1:8000/api/v1/transactions/ingest `
  -H "Content-Type: application/json" `
  -d "[{`"entity_id`":`"conta_1`",`"counterparty_id`":`"conta_2`",`"amount`":15000,`"currency`":`"BRL`",`"channel`":`"atm`",`"country`":`"BR`"}]"
```

**🍎 macOS / 🐧 Linux:**

```bash
curl -X POST http://127.0.0.1:8000/api/v1/transactions/ingest \
  -H "Content-Type: application/json" \
  -d '[{"entity_id":"conta_1","counterparty_id":"conta_2","amount":15000,"currency":"BRL","channel":"atm","country":"BR"}]'
```

---

## 🔴 Motor de Scoring de Risco

O motor de scoring (`src/intelligence/risk_engine/scoring_model.py`) é um **modelo baseado em regras transparentes**, projetado para máxima auditabilidade. Cada score pode ser rastreado até seus sinais individuais.

```
╔══════════════════════════════════════════════════════════════════════════╗
║                          SINAIS DE RISCO                                 ║
╠══════════════════════════╦═══════════════════════════════════════════════╣
║  💰  Valor               ║  Transações acima do limiar de alto valor    ║
║  🌍  Geografia           ║  Transferências internacionais               ║
║  ⚡  Velocidade          ║  Número de transações nas últimas 24h        ║
║  📦  Volume              ║  Valor total movimentado nas últimas 24h     ║
║  👥  Contrapartes        ║  Quantidade de destinos distintos em 24h     ║
║  🗺️  Desvio Geográfico   ║  Mudança de país vs. histórico recente       ║
║  ⚠️  Canal de Risco      ║  Canais críticos: ATM · Crypto               ║
╚══════════════════════════╩═══════════════════════════════════════════════╝
```

```
Score   0.0 ══════════════════════════════════════════════════ 1.0
             ║  BAIXO RISCO  ║    RISCO MÉDIO    ║ ALTO RISCO ║
             ╚═══════════════╩══════════════════╩═════════════╝
                                                        ▲
                                                ┌───────┴───────┐
                                                │ ALERTA CRIADO │
                                                │ → Push WS     │
                                                │ → DB salvo    │
                                                │ → UI flagada  │
                                                └───────────────┘
```

> Estenda o motor em `src/intelligence/risk_engine/scoring_model.py` — adicione modelos ML, features de grafos ou listas de vigilância externas sem modificar o restante do pipeline.

---

## 📁 Estrutura do Projeto

```
fraud-master-bank/
│
├── 📁 src/
│   ├── 📁 Backend/
│   │   ├── 🐍 app.py              ◀  Aplicação FastAPI · rotas e middleware
│   │   ├── 🐍 schemas.py          ◀  Modelos Pydantic · request / response
│   │   ├── 📁 services/           ◀  Camada de lógica de negócio
│   │   └── 📁 static/             ◀  Dashboard Web (HTML · CSS · JS)
│   │
│   ├── 📁 pipelines/              ◀  Pipelines de ingestão e processamento
│   │
│   ├── 📁 intelligence/
│   │   └── 📁 risk_engine/
│   │       └── 🐍 scoring_model.py  ◀  ⭐ Lógica central de scoring
│   │
│   └── 📁 db/                     ◀  Modelos ORM · sessões · migrações
│
├── 📁 data/
│   └── 🗄️ fraud_master_bank.db    ◀  Banco SQLite (criado automaticamente)
│
├── 📄 .env.example
├── 📄 requirements.txt
└── 📄 README.md
```

---

## 🧹 Reset e Limpeza de Dados

| 🪟 PowerShell | 🍎 macOS · 🐧 Linux |
|---|---|
| `Remove-Item -Force .\data\fraud_master_bank.db -ErrorAction SilentlyContinue` | `rm -f ./data/fraud_master_bank.db` |

Reinicie o servidor — o schema será recriado automaticamente.

---

## 🛠️ Solução de Problemas

<details>
<summary><strong>🔇 &nbsp; Interface carrega mas não exibe dados</strong></summary>
<br/>
O dashboard requer pelo menos uma transação. Ingira via formulário da interface ou chamando <code>/api/v1/transactions/ingest</code> diretamente pelo <code>curl</code> ou pelo Swagger UI em <code>/docs</code>.
</details>

<details>
<summary><strong>🔌 &nbsp; WebSocket aparece como "Desconectado"</strong></summary>
<br/>
Certifique-se de que o servidor está em execução e que você está acessando exatamente <code>http://127.0.0.1:8000</code>. Conexões WebSocket falharão com qualquer divergência de host ou porta.
</details>

<details>
<summary><strong>🐘 &nbsp; Erros de conexão com PostgreSQL</strong></summary>
<br/>

1. Confirme que o banco está acessível.
2. Verifique o `DATABASE_URL` no `.env`:
```dotenv
DATABASE_URL=postgresql://usuario:senha@host:5432/nome_do_banco
```
3. Garanta que o banco de destino existe antes de iniciar.
4. Verifique regras de firewall e `pg_hba.conf` em conexões remotas.
</details>

<details>
<summary><strong>📦 &nbsp; Falha na instalação de dependências</strong></summary>
<br/>

```bash
pip install --upgrade pip
pip install -r requirements.txt
```
</details>

---

## 🗺️ Roadmap

| Status | Funcionalidade |
|:---:|:---|
| ✅ | Pipeline de ingestão de transações |
| ✅ | Motor de scoring baseado em regras |
| ✅ | Alertas em tempo real via WebSocket |
| ✅ | Persistência SQLite + PostgreSQL |
| ✅ | API de gestão de investigações |
| ✅ | API de grafo de entidades |
| 🔄 | Modelo ML de scoring (XGBoost · Isolation Forest) |
| 🔄 | Rede neural de grafos para anéis de contrapartes |
| 📋 | Integração com listas de vigilância externas (OFAC · PEP) |
| 📋 | Dashboard de gestão de casos |
| 📋 | Exportação de RAS (Relatório de Atividade Suspeita) |
| 📋 | Suporte multi-tenant |
| 📋 | Ingestão via streaming Kafka / Kinesis |

---

## 🤝 Contribuição

Contribuições são bem-vindas nas seguintes áreas:

- **Novos sinais de scoring** — velocidade, centralidade de grafos, baselines comportamentais
- **Integração de modelos ML** — classificadores treinados no pipeline de scoring
- **Conectores de dados** — CSV em lote, Kafka, webhooks
- **Infraestrutura** — Docker Compose, Kubernetes, CI/CD
- **Testes** — unitários para scoring, integração para a API

---

<div align="center">

<br/>

*Construído para detectar. Projetado para explicar. Arquitetado para escalar.*

<br/>

[![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=flat-square&logo=postgresql&logoColor=white)](https://postgresql.org)
[![SQLite](https://img.shields.io/badge/SQLite-003B57?style=flat-square&logo=sqlite&logoColor=white)](https://sqlite.org)

<br/>

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:1a0000,60:DC143C,100:8B0000&height=120&section=footer&text=Fraud%20Master%20Bank%20%C2%B7%20Intelig%C3%AAncia%20Antifraude&fontSize=14&fontColor=ffcccc&fontAlignY=65&animation=fadeIn" width="100%" alt="footer"/>

</div>
