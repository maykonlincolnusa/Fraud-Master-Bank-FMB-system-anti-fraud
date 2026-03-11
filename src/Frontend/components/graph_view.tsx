import React from "react";
import { GraphSnapshot } from "../services/api_client";

type Props = { graph: GraphSnapshot | null };

export default function GraphView({ graph }: Props) {
  if (!graph) {
    return <div>Loading graph...</div>;
  }

  return (
    <div>
      Nodes: {graph.nodes.length} | Edges: {graph.edges.length}
    </div>
  );
}