import React from "react";

type EventItem = { id: string; label: string; timestamp: string };

type Props = { events: EventItem[] };

export default function TimelineView({ events }: Props) {
  if (!events.length) {
    return <div>No timeline events.</div>;
  }

  return (
    <ol>
      {events.map((event) => (
        <li key={event.id}>
          {event.label} - {event.timestamp}
        </li>
      ))}
    </ol>
  );
}