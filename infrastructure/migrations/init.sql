CREATE TABLE IF NOT EXISTS transactions (
  transaction_id VARCHAR(36) PRIMARY KEY,
  entity_id VARCHAR(128) NOT NULL,
  counterparty_id VARCHAR(128),
  amount DOUBLE PRECISION NOT NULL,
  currency VARCHAR(3) NOT NULL,
  channel VARCHAR(32),
  device_id VARCHAR(128),
  country VARCHAR(3),
  timestamp TIMESTAMP NOT NULL,
  features JSONB,
  risk_score DOUBLE PRECISION DEFAULT 0,
  risk_reasons JSONB
);

CREATE TABLE IF NOT EXISTS alerts (
  alert_id VARCHAR(36) PRIMARY KEY,
  transaction_id VARCHAR(36) NOT NULL,
  entity_id VARCHAR(128) NOT NULL,
  score DOUBLE PRECISION NOT NULL,
  reason TEXT NOT NULL,
  status VARCHAR(20) DEFAULT 'open',
  created_at TIMESTAMP DEFAULT now()
);

CREATE TABLE IF NOT EXISTS entities (
  entity_id VARCHAR(128) PRIMARY KEY,
  risk_score DOUBLE PRECISION DEFAULT 0,
  last_updated TIMESTAMP DEFAULT now()
);

CREATE TABLE IF NOT EXISTS investigations (
  case_id VARCHAR(36) PRIMARY KEY,
  alert_id VARCHAR(36) NOT NULL,
  entity_id VARCHAR(128) NOT NULL,
  status VARCHAR(20) DEFAULT 'open',
  created_at TIMESTAMP DEFAULT now()
);