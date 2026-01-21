from fastapi import APIRouter, WebSocket
import cv2
import asyncio
from app.gesture.detector import GestureDetector


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

    except Exception:
        print("WebSocket disconnected safely")

    finally:
        cap.release()
        await websocket.close()
