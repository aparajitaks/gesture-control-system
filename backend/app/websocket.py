from fastapi import APIRouter, WebSocket
import cv2
import asyncio
from app.gesture.detector import GestureDetector
from starlette.websockets import WebSocketDisconnect

router = APIRouter()
detector = GestureDetector()

@router.websocket("/ws/gesture")
async def gesture_socket(websocket: WebSocket):
    await websocket.accept()
    cap = cv2.VideoCapture(0)

    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                await asyncio.sleep(0.1)
                continue

            gesture = detector.detect_gesture(frame)
            await websocket.send_text(gesture)

            await asyncio.sleep(0.05)

    except WebSocketDisconnect:
        # Client disconnected normally (browser refresh, tab close, ngrok reconnect)
        print("Client disconnected")

    except Exception as e:
        # Any unexpected error
        print(f"Unexpected error: {e}")

    finally:
        # Always release camera
        cap.release()
        print("WebSocket cleanup complete")
