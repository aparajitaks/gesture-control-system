# ✋ Gesture Control System

Real-time Hand Gesture Detection using **MediaPipe**, **FastAPI**, and **React**

A full-stack, real-time hand gesture detection system that uses a webcam to detect and classify hand gestures and streams results live to a web dashboard using **WebSockets**.

This project demonstrates real-time Computer Vision + Full Stack Web Development integration using a clean modular architecture.

---

## 🚀 Project Overview

The **Gesture Control System** captures a live webcam stream from the browser, sends frames to a FastAPI backend through WebSockets, processes hand landmarks using MediaPipe + OpenCV, and returns real-time gesture results back to the frontend dashboard.

This enables **low-latency live gesture detection** directly inside a modern React interface.

---

## ✨ Features

- ✅ Live camera feed inside browser  
- ✅ Real-time hand landmark detection using **MediaPipe**  
- ✅ Low-latency **WebSocket** based streaming  
- ✅ FastAPI backend for gesture processing  
- ✅ React + Vite frontend with modern UI  
- ✅ Modular backend architecture (scalable + clean)  
- ✅ Real-time dashboard updates  
- ✅ Backend health-check endpoint for monitoring  
- ✅ Easy to extend for more gestures / AI classification  

---

## 🧠 Tech Stack

### Frontend
- React (Vite)
- JavaScript (ES6+)
- HTML5 Video + Canvas
- WebSocket API

### Backend
- FastAPI
- Python 3.11
- WebSockets
- MediaPipe
- OpenCV

---

## 🏗️ System Architecture

```text
Webcam
   ↓
Browser (React Frontend)
   ↓ WebSocket
FastAPI Backend
   ↓
MediaPipe + OpenCV
   ↓
Gesture Detection & Classification
   ↓ WebSocket Response
Live Dashboard Update

⚙️ How to Run Locally
1️⃣ Clone the Repository
git clone https://github.com/aparajitaks/gesture-control-system.git
cd gesture-control-system

2️⃣ Backend Setup (FastAPI)
cd backend
python3.11 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000


Backend runs at:

👉 http://localhost:8000

3️⃣ Frontend Setup (React + Vite)

Open a new terminal:

cd frontend
npm install
npm run dev


Frontend runs at:

👉 http://localhost:5173

🌐 API Endpoints
Health Check
GET /health


Response:

{
  "status": "ok"
}

WebSocket Connection
/ws


Used for real-time video frame transfer + gesture response streaming.

🎥 Demo Video

📌 YouTube Demo:
https://www.youtube.com/watch?v=6uV31eVAnpI

📂 Folder Structure
gesture-control-system/
│
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── websocket.py
│   │   ├── gesture_detector.py
│   │   └── utils/
│   ├── requirements.txt
│   └── README.md (optional)
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   └── App.jsx
│   ├── package.json
│   └── vite.config.js
│
└── README.md

🎯 Learning Outcomes

Real-time WebSocket communication

MediaPipe hand landmark detection pipeline

Integrating React frontend with FastAPI backend

Debugging WebSocket lifecycle + streaming issues

Building scalable modular backend architecture

Practical real-time computer vision implementation

🔮 Future Improvements

Add gesture-to-action mapping (volume, scrolling, app control)

Add ML-based gesture classification model

Improve UI dashboard analytics

Add multi-hand detection support

Deploy using Docker + Cloud hosting
