# ✋ Gesture Control System

**Real-time Hand Gesture Detection using MediaPipe, FastAPI & React**

A full-stack, real-time hand gesture detection system that uses a webcam to detect and classify hand gestures and streams results live to a web dashboard using WebSockets.

---

## 🚀 Features

- 📷 **Live camera feed in browser**
- ✋ **Real-time hand detection using MediaPipe**
- ⚡ **Low-latency WebSocket communication**
- 🧠 **FastAPI backend for gesture processing**
- 🎨 **Modern React + Vite frontend**
- 🧩 **Clean, modular & extensible architecture**
- ❤️ **Health-check API for backend monitoring**

---

## 🧠 Tech Stack

### Frontend
- React (Vite)
- JavaScript (ES6+)
- HTML5 Video & Canvas
- WebSocket API

### Backend
- FastAPI
- WebSockets
- MediaPipe
- OpenCV
- Python 3.11

---

## 🏗️ System Architecture
Webcam
↓
Browser (React)
↓ WebSocket
FastAPI Backend
↓
MediaPipe + OpenCV
↓
Gesture Classification
↓
Live Dashboard Update



---

## 📂 Project Structure

gesture-control-system/
│
├── backend/
│ ├── app/
│ │ ├── api/
│ │ │ └── health.py # Health check endpoint
│ │ ├── core/
│ │ │ ├── config.py # App configuration
│ │ │ └── logger.py # Logging setup
│ │ ├── gesture/
│ │ │ ├── detector.py # Hand detection logic
│ │ │ ├── controller.py # Gesture decision layer
│ │ │ └── utils.py # Helper functions
│ │ ├── websocket.py # WebSocket handler
│ │ └── main.py # FastAPI entry point
│ │
│ ├── requirements.txt
│ └── run.sh
│
├── frontend/
│ ├── src/
│ │ ├── components/
│ │ │ ├── Camera.jsx
│ │ │ ├── Control.jsx
│ │ │ └── Dashboard.jsx
│ │ ├── pages/
│ │ │ └── Home.jsx
│ │ ├── App.jsx
│ │ └── main.jsx
│ ├── index.html
│ └── vite.config.js
│
├── .gitignore
└── README.md


---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/aparajitaks/gesture-control-system.git
cd gesture-control-system


2️⃣ Backend Setup
cd backend
python3.11 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000


Backend runs at:
👉 http://localhost:8000

3️⃣ Frontend Setup
cd frontend
npm install
npm run dev


Frontend runs at:
👉 http://localhost:5173


🎯 Learning Outcomes

Real-time WebSocket communication

MediaPipe hand landmark processing

Full-stack architecture with React + FastAPI

Clean backend modularization

Debugging WebSocket lifecycle issues

Practical real-time computer vision integration