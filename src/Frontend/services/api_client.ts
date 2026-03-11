export const API_BASE = "/api/v1";

export type Alert = {
  alert_id: string;
  transaction_id: string;
  entity_id: string;
  score: number;
  reason: string;
  status: string;
  created_at: string;
};

export type Entity = {
  entity_id: string;
  risk_score: number;
  last_updated: string;
};

export type GraphSnapshot = {
  nodes: { id: string; type: string }[];
  edges: { source: string; target: string; weight: number }[];
};

export async function getAlerts(): Promise<Alert[]> {
  const res = await fetch(`${API_BASE}/alerts`);
  return res.json();
}

export async function getEntities(): Promise<Entity[]> {
  const res = await fetch(`${API_BASE}/entities`);
  return res.json();
}

export async function getGraph(): Promise<GraphSnapshot> {
  const res = await fetch(`${API_BASE}/graph`);
  return res.json();
}