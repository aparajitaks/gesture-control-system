import { useEffect, useState } from "react";
import Camera from "../components/Camera";

export default function Home() {
  const [gesture, setGesture] = useState("WAITING");

  useEffect(() => {
    const ws = new WebSocket("ws://127.0.0.1:8000/ws/gesture");

    ws.onmessage = (event) => {
      setGesture(event.data);
    };

    ws.onerror = (err) => {
      console.error("WebSocket error", err);
    };

    return () => ws.close();
  }, []);

  const colorMap = {
    HAND_DETECTED: "green",
    WAITING: "gray",
    NO_CAMERA: "red",
  };

  return (
    <div style={{ padding: 20 }}>
      <h1>✋ Gesture Control System</h1>
      <h2 style={{ color: colorMap[gesture] }}>
        Gesture: {gesture}
      </h2>
      <Camera />
    </div>
  );
}
