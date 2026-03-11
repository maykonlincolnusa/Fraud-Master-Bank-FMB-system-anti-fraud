import { useEffect, useState } from "react";
import { GraphSnapshot, getGraph } from "../services/api_client";

export function useGraph(): GraphSnapshot | null {
  const [graph, setGraph] = useState<GraphSnapshot | null>(null);

  useEffect(() => {
    let active = true;
    getGraph().then((data) => {
      if (active) {
        setGraph(data);
      }
    });
    return () => {
      active = false;
    };
  }, []);

  return graph;
}