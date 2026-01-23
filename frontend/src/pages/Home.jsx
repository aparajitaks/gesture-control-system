import { useEffect, useState } from "react";
import Camera from "../components/Camera";
import "../styles/Home.css";

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

  const gestureDescriptions = {
    HAND_DETECTED: "Hand detected",
    WAITING: "Waiting for gesture",
    NO_CAMERA: "No camera detected",
  };

  return (
    <div className="dashboard-container">
      <header className="dashboard-header">
        <div className="header-content">
          <h1>AI Gesture Control Dashboard</h1>
          <p className="subtext">
            Real-time Computer Vision • Hand Gesture Recognition
          </p>
        </div>
        <div className="status-badges">
          <span className="badge online">System Online</span>
          <span className="badge camera">Camera Active</span>
          <span className="badge ai">AI Model Running</span>
        </div>
      </header>

      <main className="dashboard-main">
        <div
          className={`live-feed-card ${
            gesture !== "WAITING" ? "active" : "idle"
          }`}
        >
          <div className="live-indicator">
            <span className="dot"></span> LIVE
          </div>
          <Camera />
          <div className="ai-processing">AI Processing...</div>
          <div className="live-feed-label">Live Camera Feed</div>
        </div>

        <div className="gesture-panel">
          <div className="gesture-status">
            <h2 className={gesture !== "WAITING" ? "highlight" : ""}>
              {gestureDescriptions[gesture] || gesture}
            </h2>
          </div>

          <div className="control-panel">
            <h3>Gesture Commands</h3>
            <ul>
              <li>✊ Fist → Action 1</li>
              <li>✌️ Peace → Action 2</li>
              <li>🖐️ Open Hand → Action 3</li>
            </ul>
          </div>
        </div>
      </main>
    </div>
  );
}
