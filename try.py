// components/IndiaLeafletMap.jsx
"use client";
import React, { useEffect } from "react";
import dynamic from "next/dynamic";
import "leaflet/dist/leaflet.css";

// Dynamically import react-leaflet components (so import only client-side)
const MapContainer = dynamic(() => import("react-leaflet").then(mod => mod.MapContainer), { ssr: false });
const TileLayer = dynamic(() => import("react-leaflet").then(mod => mod.TileLayer), { ssr: false });
const Marker = dynamic(() => import("react-leaflet").then(mod => mod.Marker), { ssr: false });
const Popup = dynamic(() => import("react-leaflet").then(mod => mod.Popup), { ssr: false });

// If you want clustering, install react-leaflet-markercluster and import dynamically similarly.

const learners = [
  { id: 1, name: "Asha", city: "Bengaluru", state: "Karnataka", lat: 12.9716, lng: 77.5946, progressPct: 78 },
  { id: 2, name: "Ravi", city: "Mumbai", state: "Maharashtra", lat: 19.0760, lng: 72.8777, progressPct: 45 },
  // ...
];

export default function IndiaLeafletMap() {
  // map bounds roughly covering India — adjust if you want tighter bounds
  const indiaCenter = [22.0, 79.0];
  const initialZoom = 5;

  return (
    <div style={{ height: "700px", width: "100%" }}>
      <MapContainer center={indiaCenter} zoom={initialZoom} style={{ height: "100%", width: "100%" }} whenCreated={(map) => {
        // Optionally restrict bounds to India bbox to avoid panning away
        // map.setMaxBounds([[6, 68], [36, 98]]);
      }}>
        <TileLayer
          attribution='© OpenStreetMap contributors'
          url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
        />

        {learners.map(l => (
          <Marker key={l.id} position={[l.lat, l.lng]}>
            <Popup>
              <div>
                <strong>{l.name}</strong><br />
                {l.city}, {l.state}<br />
                Progress: {l.progressPct}%<br />
                <a href={`/learners/${l.id}`}>View profile</a>
              </div>
            </Popup>
          </Marker>
        ))}
      </MapContainer>
    </div>
  );
}
