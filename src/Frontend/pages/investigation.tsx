import React from "react";
import TimelineView from "../components/timeline_view";

export default function InvestigationPage() {
  return (
    <div>
      <h1>Investigation</h1>
      <TimelineView events={[]} />
    </div>
  );
}