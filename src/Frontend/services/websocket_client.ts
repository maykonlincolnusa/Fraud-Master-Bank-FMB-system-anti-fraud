export function createAlertsSocket(onMessage: () => void): WebSocket {
  const ws = new WebSocket(`${window.location.origin.replace("http", "ws")}/ws/alerts`);
  ws.addEventListener("message", onMessage);
  return ws;
}