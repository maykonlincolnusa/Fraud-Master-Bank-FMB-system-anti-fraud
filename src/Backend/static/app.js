const apiBase = `${window.location.origin}/api/v1`;

const alertList = document.getElementById("alertsList");
const entityList = document.getElementById("entitiesList");
const ingestForm = document.getElementById("ingestForm");
const ingestResult = document.getElementById("ingestResult");
const apiStatus = document.getElementById("apiStatus");
const wsStatus = document.getElementById("wsStatus");
const entityCount = document.getElementById("entityCount");
const graphCount = document.getElementById("graphCount");
const graphNodes = document.getElementById("graphNodes");
const graphEdges = document.getElementById("graphEdges");
const graphTop = document.getElementById("graphTop");

async function checkHealth() {
  try {
    const res = await fetch(`${window.location.origin}/health`);
    apiStatus.textContent = res.ok ? "online" : "offline";
    apiStatus.style.background = res.ok ? "#d0f0f2" : "#ffe8d2";
  } catch {
    apiStatus.textContent = "offline";
  }
}

function renderAlerts(alerts) {
  alertList.innerHTML = "";
  if (!alerts.length) {
    alertList.innerHTML = "<li>No alerts yet.</li>";
    return;
  }
  alerts.slice(0, 8).forEach((alert) => {
    const li = document.createElement("li");
    li.innerHTML = `<strong>${alert.reason}</strong>
      <span>Entity: ${alert.entity_id}</span>
      <span>Score: ${alert.score.toFixed(2)}</span>`;
    alertList.appendChild(li);
  });
}

function renderEntities(entities) {
  entityList.innerHTML = "";
  entityCount.textContent = entities.length;
  if (!entities.length) {
    entityList.innerHTML = "<li>No entities yet.</li>";
    return;
  }
  entities.slice(0, 8).forEach((entity) => {
    const li = document.createElement("li");
    li.innerHTML = `<strong>${entity.entity_id}</strong>
      <span>Risk: ${entity.risk_score.toFixed(2)}</span>`;
    entityList.appendChild(li);
  });
}

function renderGraph(graph) {
  graphNodes.textContent = graph.nodes.length;
  graphEdges.textContent = graph.edges.length;
  graphCount.textContent = `${graph.nodes.length} / ${graph.edges.length}`;
  if (!graph.edges.length) {
    graphTop.textContent = "-";
    return;
  }
  const top = graph.edges.reduce((a, b) => (a.weight > b.weight ? a : b));
  graphTop.textContent = `${top.source} → ${top.target} (${top.weight})`;
}

async function refreshAlerts() {
  const res = await fetch(`${apiBase}/alerts`);
  const data = await res.json();
  renderAlerts(data);
}

async function refreshEntities() {
  const res = await fetch(`${apiBase}/entities`);
  const data = await res.json();
  renderEntities(data);
}

async function refreshGraph() {
  const res = await fetch(`${apiBase}/graph`);
  const data = await res.json();
  renderGraph(data);
}

ingestForm.addEventListener("submit", async (event) => {
  event.preventDefault();
  ingestResult.textContent = "sending...";
  const formData = new FormData(ingestForm);
  const payload = [
    {
      entity_id: formData.get("entity_id"),
      counterparty_id: formData.get("counterparty_id") || null,
      amount: Number(formData.get("amount")),
      currency: (formData.get("currency") || "USD").toString().toUpperCase(),
      channel: formData.get("channel") || null,
      country: formData.get("country") || null,
    },
  ];

  try {
    const res = await fetch(`${apiBase}/transactions/ingest`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload),
    });
    const data = await res.json();
    ingestResult.textContent = `ingested ${data.transactions.length} tx`;
    await refreshAlerts();
    await refreshEntities();
    await refreshGraph();
  } catch (err) {
    ingestResult.textContent = "failed to ingest";
  }
});

function connectWebSocket() {
  const ws = new WebSocket(`ws://${window.location.host}/ws/alerts`);
  ws.addEventListener("open", () => {
    wsStatus.textContent = "connected";
    wsStatus.style.background = "#d0f0f2";
  });
  ws.addEventListener("close", () => {
    wsStatus.textContent = "disconnected";
    wsStatus.style.background = "#ffe8d2";
    setTimeout(connectWebSocket, 1500);
  });
  ws.addEventListener("message", async () => {
    await refreshAlerts();
  });
}

checkHealth();
refreshAlerts();
refreshEntities();
refreshGraph();
connectWebSocket();
