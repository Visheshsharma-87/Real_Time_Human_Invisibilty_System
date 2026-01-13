import cv2
import time

class FPSCounter:
    def __init__(self):
        self.prev = time.time()

    def update(self):
        now = time.time()
        fps = 1 / (now - self.prev + 1e-6)
        self.prev = now
        return int(fps)

def draw_text(frame, text, pos, scale=0.8):
    cv2.putText(
        frame, text, pos,
        cv2.FONT_HERSHEY_SIMPLEX,
        scale, (0, 255, 0), 2
    )
