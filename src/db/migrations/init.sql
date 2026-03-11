CREATE TABLE accounts (
  id BIGINT PRIMARY KEY,
  created_at TIMESTAMP DEFAULT now(),
  metadata JSONB
);

CREATE TABLE transactions (
  id BIGSERIAL PRIMARY KEY,
  src_account BIGINT,
  dst_account BIGINT,
  amount numeric,
  tx_type varchar(50),
  ts TIMESTAMP DEFAULT now(),
  raw JSONB
);

CREATE TABLE alerts (
  id BIGSERIAL PRIMARY KEY,
  transaction_id BIGINT,
  score numeric,
  reason TEXT,
  created_at TIMESTAMP DEFAULT now(),
  status VARCHAR(20) DEFAULT 'open'
);