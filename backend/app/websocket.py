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
            try:
                await websocket.send_text(gesture)
            except WebSocketDisconnect:
                print("WebSocket disconnected safely")
                break

            await asyncio.sleep(0.05)

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        cap.release()
        try:
            await websocket.close()
        except WebSocketDisconnect:
            pass
