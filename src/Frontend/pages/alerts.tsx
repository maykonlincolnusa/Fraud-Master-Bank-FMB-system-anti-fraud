import React from "react";
import AlertsPanel from "../components/alerts_oanel";
import { useAlerts } from "../hooks/usealerts";

export default function AlertsPage() {
  const alerts = useAlerts();

  return (
    <div>
      <h1>Alerts</h1>
      <AlertsPanel alerts={alerts} />
    </div>
  );
}