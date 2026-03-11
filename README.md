<div align="center">

```
 ▄████████    ▄████████    ▄████████ ███    █▄  ████████▄
███    ███   ███    ███   ███    ███ ███    ███ ███   ▀███
███    █▀    ███    ███   ███    ███ ███    ███ ███    ███
███         ▄███▄▄▄▄██▀   ███    ███ ███    ███ ███    ███
███        ▀▀███▀▀▀▀▀   ▀███████████ ███    ███ ███    ███
███    █▄  ▀███████████   ███    ███ ███    ███ ███    ███
███    ███   ███    ███   ███    ███ ███    ███ ███   ▄███
████████▀    ███    ███   ███    █▀  ████████▀  ████████▀

███▄▄▄▄      ▄██████▄     ▄████████    ▄████████     ▄████████
███▀▀▀██▄   ███    ███   ███    ███   ███    ███    ███    ███
███   ███   ███    ███   ███    █▀    ███    █▀     ███    █▀
███   ███   ███    ███  ▄███▄▄▄       ███          ▄███▄▄▄
███   ███   ███    ███ ▀▀███▀▀▀     ▀███████████  ▀▀███▀▀▀
███   ███   ███    ███   ███    █▄           ███    ███    █▄
███   ███   ███    ███   ███    ███    ▄█    ███    ███    ███
 ▀█   █▀     ▀██████▀   ██████████  ▄████████▀     ██████████

              ███████▄    ▄████████ ███▄▄▄▄   ████████▄
              ███   ███  ███    ███ ███▀▀▀██▄ ███   ▀███
              ███   ███  ███    ███ ███   ███ ███    ███
              ███   ███  ███    ███ ███   ███ ███   ▄███
              ███   ███  ███    ███ ███   ███ ███  ▀▀██████
              ███   ███  ███    ███ ███   ███ ███    ███
              ███   ███  ███    ███ ███   ███ ███   ▄███
              ████████▀   ▀██████▀   ▀█   █▀  ████████▀
```

<br/>

### `[ INTELIGÊNCIA ANTIFRAUDE · TEMPO REAL · PRODUÇÃO ]`

<br/>

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.111+-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-Padrão-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Opcional-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)
![WebSocket](https://img.shields.io/badge/WebSocket-Alertas%20ao%20Vivo-E34F26?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Operacional-00C9A7?style=for-the-badge)
![Licença](https://img.shields.io/badge/Licença-Proprietária-DC143C?style=for-the-badge)

<br/>

> **Plataforma operacional de detecção de fraudes bancárias** — ingestão de transações em tempo real, enriquecimento de features comportamentais, scoring de risco com explicabilidade total e alertas ao vivo via WebSocket.
>
> Sem caixas-pretas. Sem dados simulados. Sem pipelines de brinquedo.
> **Este é um sistema real — pronto para executar, estender e implantar.**

</div>

---

<br/>

## ◈ Índice

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

<br/>

---

## ⚡ O que é o Fraud Master Bank?

O **Fraud Master Bank** é uma plataforma antifraude completa, operacional e de nível produção — construída sobre **FastAPI** com suporte a banco de dados dual (SQLite / PostgreSQL), WebSocket em tempo real e um motor de scoring totalmente auditável.

Cada transação ingerida passa por um pipeline completo:

```
  INGESTÃO  ──▶  ENRIQUECIMENTO  ──▶  SCORING  ──▶  ALERTA  ──▶  DASHBOARD
```

Nenhuma etapa é simulada. Tudo é persistido, rastreável e extensível.

<br/>

---

## 🧠 Visão Geral do Sistema

```
╔══════════════════════════════════════════════════════════════════════════╗
║                        FRAUD MASTER BANK                                 ║
║                                                                           ║
║   ┌──────────────┐    ┌───────────────────┐    ┌──────────────────────┐ ║
║   │  API REST    │───▶│    INGESTÃO       │───▶│  ENRIQUECIMENTO      │ ║
║   │ POST /ingest │    │    Pipeline       │    │  · Velocidade (24h)  │ ║
║   └──────────────┘    └───────────────────┘    │  · Volume total      │ ║
║                                                 │  · Nº contrapartes   │ ║
║   ┌──────────────┐                             │  · Desvio geográfico │ ║
║   │ Formulário   │────────────────────────────▶└──────────┬───────────┘ ║
║   │  Web UI      │                                        │             ║
║   └──────────────┘                                        ▼             ║
║                                               ┌──────────────────────┐  ║
║                                               │   MOTOR DE RISCO     │  ║
║                                               │   Scoring Engine     │  ║
║                                               └──────────┬───────────┘  ║
║                                                          │              ║
║                          ┌───────────────────────────────┤              ║
║                          ▼                               ▼              ║
║              ┌──────────────────────┐      ┌──────────────────────┐    ║
║              │  BANCO DE DADOS      │      │  STREAM WEBSOCKET    │    ║
║              │  SQLite / Postgres   │      │  /ws/alerts          │    ║
║              └──────────┬───────────┘      └──────────────────────┘    ║
║                         │                                               ║
║                         ▼                                               ║
║              ┌──────────────────────┐                                  ║
║              │  DASHBOARD WEB       │                                  ║
║              │  http://localhost    │                                  ║
║              └──────────────────────┘                                  ║
╚══════════════════════════════════════════════════════════════════════════╝
```

<br/>

---

## 🚀 Início Rápido

### Passo 1 — Clone o repositório e crie o ambiente virtual

```bash
git clone https://github.com/sua-org/fraud-master-bank.git
cd fraud-master-bank
python -m venv .venv
```

---

### Passo 2 — Ative o ambiente e instale as dependências

<table>
<tr>
<th align="center">🪟 &nbsp; Windows · PowerShell</th>
<th align="center">🍎 macOS &nbsp;·&nbsp; 🐧 Linux</th>
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

---

### Passo 3 — Abra no navegador

| Interface | Endereço |
|:---|:---|
| 🖥️ **Dashboard** | [`http://127.0.0.1:8000`](http://127.0.0.1:8000) |
| 📡 **API REST** | [`http://127.0.0.1:8000/api/v1`](http://127.0.0.1:8000/api/v1) |
| 🔴 **WebSocket — Alertas ao Vivo** | `ws://127.0.0.1:8000/ws/alerts` |
| 📖 **Documentação Swagger** | [`http://127.0.0.1:8000/docs`](http://127.0.0.1:8000/docs) |

<br/>

---

## 💾 Persistência e Banco de Dados

O sistema suporta dois backends de banco de dados. O **SQLite funciona imediatamente**, sem nenhuma configuração. O schema é criado automaticamente na inicialização da aplicação.

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
║  📁  ./data/fraud_master_     ║  🌐  DATABASE_URL configurável      ║
║      bank.db                  ║                                      ║
╚═══════════════════════════════╩══════════════════════════════════════╝
```

### Migrando para PostgreSQL

**Passo 1** — Copie o arquivo de variáveis de ambiente:

```bash
cp .env.example .env
```

**Passo 2** — Edite o `.env` com sua string de conexão:

```dotenv
DATABASE_URL=postgresql://usuario:senha@host:5432/nome_do_banco
```

**Passo 3** — Reinicie o servidor. A migração de schema ocorre automaticamente.

<br/>

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
| `POST` | `/api/v1/investigations` | Abrir uma nova investigação |
| `PATCH` | `/api/v1/investigations/{id}` | Atualizar status de investigação |
| `WS` | `/ws/alerts` | Stream de alertas em tempo real via WebSocket |

<br/>

---

## 🔌 Ingestão de Transações

Envie um array JSON ao endpoint de ingestão. O pipeline irá **enriquecer features**, **calcular o score de risco**, **persistir no banco** e **disparar alertas via WebSocket** — tudo em uma única requisição.

### Schema da Transação

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

### Enviando uma transação

<table>
<tr>
<th align="center">🪟 &nbsp; PowerShell</th>
</tr>
<tr>
<td>

```powershell
curl -X POST http://127.0.0.1:8000/api/v1/transactions/ingest `
  -H "Content-Type: application/json" `
  -d "[{`"entity_id`":`"conta_1`",`"counterparty_id`":`"conta_2`",`"amount`":15000,`"currency`":`"BRL`",`"channel`":`"atm`",`"country`":`"BR`"}]"
```

</td>
</tr>
<tr>
<th align="center">🍎 macOS &nbsp;·&nbsp; 🐧 Linux</th>
</tr>
<tr>
<td>

```bash
curl -X POST http://127.0.0.1:8000/api/v1/transactions/ingest \
  -H "Content-Type: application/json" \
  -d '[{"entity_id":"conta_1","counterparty_id":"conta_2","amount":15000,"currency":"BRL","channel":"atm","country":"BR"}]'
```

</td>
</tr>
</table>

<br/>

---

## 🔴 Motor de Scoring de Risco

O motor de scoring (`src/intelligence/risk_engine/scoring_model.py`) é um **modelo baseado em regras transparentes**, projetado para máxima auditabilidade e explicabilidade. Cada score pode ser rastreado até seus sinais individuais.

```
╔══════════════════════════════════════════════════════════════════════════╗
║                        SINAIS DE RISCO                                   ║
╠══════════════════════════╦═══════════════════════════════════════════════╣
║  SINAL                   ║  DESCRIÇÃO                                   ║
╠══════════════════════════╬═══════════════════════════════════════════════╣
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
                     Score de Risco → Geração de Alerta

   0.0 ══════════════════════════════════════════════════════ 1.0
        ║   BAIXO RISCO  ║     RISCO MÉDIO     ║ ALTO RISCO  ║
        ╚════════════════╩════════════════════╩══════════════╝
                                                      ▲
                                              ┌───────┴────────┐
                                              │  ALERTA CRIADO │
                                              │ → Push WS      │
                                              │ → DB salvo     │
                                              │ → UI sinaliza  │
                                              └────────────────┘
```

> Estenda o modelo em `src/intelligence/risk_engine/scoring_model.py` — adicione modelos ML, features de grafos ou listas de vigilância externas sem modificar o restante do pipeline.

<br/>

---

## 📁 Estrutura do Projeto

```
fraud-master-bank/
│
├── 📁 src/
│   │
│   ├── 📁 Backend/
│   │   ├── 🐍 app.py                   ◀  Aplicação FastAPI · rotas e middleware
│   │   ├── 🐍 schemas.py               ◀  Modelos Pydantic · request / response
│   │   ├── 📁 services/                ◀  Camada de lógica de negócio
│   │   └── 📁 static/                  ◀  Dashboard Web (HTML · CSS · JS)
│   │
│   ├── 📁 pipelines/                   ◀  Pipelines de ingestão e processamento
│   │
│   ├── 📁 intelligence/
│   │   └── 📁 risk_engine/
│   │       └── 🐍 scoring_model.py     ◀  ⭐ Lógica central de scoring de fraude
│   │
│   └── 📁 db/                          ◀  Modelos ORM · sessões · migrações
│
├── 📁 data/
│   └── 🗄️  fraud_master_bank.db        ◀  Banco SQLite (criado automaticamente)
│
├── 📄 .env.example                     ◀  Template de variáveis de ambiente
├── 📄 requirements.txt                 ◀  Dependências Python
└── 📄 README.md
```

<br/>

---

## 🧹 Reset e Limpeza de Dados

Para apagar todos os dados e reiniciar do zero:

<table>
<tr>
<th align="center">🪟 &nbsp; PowerShell</th>
<th align="center">🍎 macOS &nbsp;·&nbsp; 🐧 Linux</th>
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

Reinicie o servidor — o schema será recriado automaticamente.

<br/>

---

## 🛠️ Solução de Problemas

<details>
<summary><strong>🔇 &nbsp; Interface carrega mas não exibe dados</strong></summary>
<br/>

O dashboard requer pelo menos uma transação para exibir informações. Ingira uma transação pelo formulário da interface ou chamando diretamente o endpoint `/api/v1/transactions/ingest` via `curl` ou pelo Swagger UI em `/docs`.

</details>

<details>
<summary><strong>🔌 &nbsp; WebSocket aparece como "Desconectado"</strong></summary>
<br/>

Certifique-se de que o servidor da API está em execução (`uvicorn ... --reload`) e que você está acessando a aplicação pelo endereço exato `http://127.0.0.1:8000`. Conexões WebSocket falharão se houver divergência de host ou porta entre a origem da página e o endpoint WS.

</details>

<details>
<summary><strong>🐘 &nbsp; Erros de conexão com PostgreSQL</strong></summary>
<br/>

1. Confirme que o servidor de banco de dados está acessível a partir da sua máquina.
2. Verifique se o `DATABASE_URL` no arquivo `.env` está correto:
   ```dotenv
   DATABASE_URL=postgresql://usuario:senha@host:5432/nome_do_banco
   ```
3. Garanta que o banco de dados de destino existe antes de iniciar a aplicação.
4. Verifique regras de firewall e o arquivo `pg_hba.conf` em conexões remotas.

</details>

<details>
<summary><strong>📦 &nbsp; Falha na instalação de dependências</strong></summary>
<br/>

Verifique se você possui Python 3.10+ e que o ambiente virtual está ativado antes de executar o `pip install`. Em alguns sistemas pode ser necessário atualizar o pip primeiro:

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

</details>

<br/>

---

## 🗺️ Roadmap

| Status | Funcionalidade |
|:---:|:---|
| ✅ Concluído | Pipeline de ingestão de transações |
| ✅ Concluído | Motor de scoring baseado em regras |
| ✅ Concluído | Alertas em tempo real via WebSocket |
| ✅ Concluído | Persistência SQLite + PostgreSQL |
| ✅ Concluído | API de gestão de investigações |
| ✅ Concluído | API de grafo de entidades |
| 🔄 Em andamento | Modelo ML de scoring (XGBoost · Isolation Forest) |
| 🔄 Em andamento | Rede neural de grafos para anéis de contrapartes |
| 📋 Planejado | Integração com listas de vigilância externas (OFAC · PEP) |
| 📋 Planejado | Dashboard de gestão de casos |
| 📋 Planejado | Exportação de RAS (Relatório de Atividade Suspeita) |
| 📋 Planejado | Suporte multi-tenant |
| 📋 Planejado | Ingestão via streaming Kafka / Kinesis |

<br/>

---

## 🤝 Contribuição

Contribuições são bem-vindas nas seguintes áreas:

- **Novos sinais de scoring** — padrões de velocidade, centralidade de grafos, baselines comportamentais
- **Integração de modelos ML** — conectar classificadores treinados ao pipeline de scoring
- **Conectores de dados** — novos formatos de ingestão (CSV em lote, Kafka, webhook)
- **Infraestrutura** — Docker Compose, manifestos Kubernetes, pipelines de CI/CD
- **Testes** — testes unitários para a lógica de scoring e testes de integração da API

<br/>

---

<div align="center">

```
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║            F R A U D   M A S T E R   B A N K                ║
║                                                              ║
║        Plataforma de Inteligência Antifraude                 ║
║                                                              ║
║   Construído para detectar. Projetado para explicar.         ║
║              Arquitetado para escalar.                       ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
```

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=flat-square&logo=postgresql&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=flat-square&logo=sqlite&logoColor=white)

</div>
