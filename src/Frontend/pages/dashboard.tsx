import React from "react";
import AlertsPanel from "../components/alerts_oanel";
import GraphView from "../components/graph_view";
import { useAlerts } from "../hooks/usealerts";
import { useGraph } from "../hooks/useGraph";

export default function Dashboard() {
  const alerts = useAlerts();
  const graph = useGraph();

  return (
    <div>
      <h1>Fraud Dashboard</h1>
      <section>
        <h2>Alerts</h2>
        <AlertsPanel alerts={alerts} />
      </section>
      <section>
        <h2>Graph Snapshot</h2>
        <GraphView graph={graph} />
      </section>
    </div>
  );
}