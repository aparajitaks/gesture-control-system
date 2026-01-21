import cv2
import mediapipe as mp
import time

mp_hands = mp.solutions.hands

class GestureDetector:
    def __init__(self):
        self.hands = mp_hands.Hands(
            static_image_mode=False,
            max_num_hands=1,
            min_detection_confidence=0.7,
            min_tracking_confidence=0.7
        )

        self.last_gesture = "WAITING"
        self.last_time = time.time()

    def _finger_states(self, landmarks, hand_label):
        """
        Returns finger states:
        [thumb, index, middle, ring, pinky]
        """
        tips = [4, 8, 12, 16, 20]
        pips = [3, 6, 10, 14, 18]

        fingers = []

        # ✅ THUMB (depends on hand side)
        if hand_label == "Right":
            fingers.append(landmarks[tips[0]].x < landmarks[pips[0]].x)
        else:  # Left hand
            fingers.append(landmarks[tips[0]].x > landmarks[pips[0]].x)

        # ✅ Other fingers (vertical)
        for i in range(1, 5):
            fingers.append(
                landmarks[tips[i]].y < landmarks[pips[i]].y
            )

        return fingers

    def detect_gesture(self, frame):
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = self.hands.process(frame_rgb)

        if not result.multi_hand_landmarks:
            return "WAITING"

        hand_landmarks = result.multi_hand_landmarks[0]
        hand_label = result.multi_handedness[0].classification[0].label

        lm = hand_landmarks.landmark
        fingers = self._finger_states(lm, hand_label)

        # 🧠 GESTURE RULES
        if fingers == [False, True, True, False, False]:
            gesture = "PEACE"
        elif fingers == [False, False, False, False, False]:
            gesture = "FIST"
        elif fingers == [True, True, True, True, True]:
            gesture = "OPEN_PALM"
        else:
            gesture = "HAND_DETECTED"

        # ⏱ Stability (anti-flicker)
        now = time.time()
        if gesture != self.last_gesture and now - self.last_time < 0.3:
            return self.last_gesture

        self.last_gesture = gesture
        self.last_time = now
        return gesture
