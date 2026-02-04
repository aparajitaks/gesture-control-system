from fastapi import APIRouter, WebSocket
from starlette.websockets import WebSocketDisconnect
import cv2
import asyncio

from app.gesture.detector import GestureDetector

router = APIRouter()
detector = GestureDetector()


@router.websocket("/ws/gesture")
async def gesture_socket(websocket: WebSocket):
    await websocket.accept()
    print("WebSocket connected")

    cap = cv2.VideoCapture(0)

    try:
        while True:
            # If camera is not available, keep socket alive and retry
            if not cap.isOpened():
                try:
                    await websocket.send_text("NO_CAMERA")
                except WebSocketDisconnect:
                    break

                await asyncio.sleep(1)
                cap.open(0)
                continue

            ret, frame = cap.read()
            if not ret:
                await asyncio.sleep(0.05)
                continue

            try:
                gesture = detector.detect_gesture(frame)
            except Exception as e:
                print("Detector error:", e)
                gesture = "WAITING"

            if not gesture:
                gesture = "WAITING"

            try:
                await websocket.send_text(gesture)
            except WebSocketDisconnect:
                break

            await asyncio.sleep(0.05)

    except Exception as e:
        print("Unexpected error:", e)

    finally:
        cap.release()
        print("Camera released, WebSocket closed")
