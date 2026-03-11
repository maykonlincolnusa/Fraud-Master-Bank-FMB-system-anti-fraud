import React from "react";

type Props = { countries: string[] };

export default function FraudMap({ countries }: Props) {
  if (!countries.length) {
    return <div>No geo activity yet.</div>;
  }

  return (
    <div>
      Active countries: {countries.join(", ")}
    </div>
  );
}