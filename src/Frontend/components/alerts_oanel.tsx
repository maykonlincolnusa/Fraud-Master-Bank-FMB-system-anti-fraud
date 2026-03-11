import React from "react";
import { Alert } from "../services/api_client";

type Props = { alerts: Alert[] };

export default function AlertsPanel({ alerts }: Props) {
  if (!alerts.length) {
    return <div>No alerts yet.</div>;
  }

  return (
    <ul>
      {alerts.slice(0, 8).map((alert) => (
        <li key={alert.alert_id}>
          <strong>{alert.reason}</strong>
          <div>Entity: {alert.entity_id}</div>
          <div>Score: {alert.score.toFixed(2)}</div>
        </li>
      ))}
    </ul>
  );
}