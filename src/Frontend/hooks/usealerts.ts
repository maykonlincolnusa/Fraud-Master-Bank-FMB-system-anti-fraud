import { useEffect, useState } from "react";
import { Alert, getAlerts } from "../services/api_client";

export function useAlerts(): Alert[] {
  const [alerts, setAlerts] = useState<Alert[]>([]);

  useEffect(() => {
    let active = true;
    getAlerts().then((data) => {
      if (active) {
        setAlerts(data);
      }
    });
    return () => {
      active = false;
    };
  }, []);

  return alerts;
}