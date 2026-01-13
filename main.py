import cv2
import time
import numpy as np
import mediapipe as mp
from utils import FPSCounter, draw_text

cap = cv2.VideoCapture(0)

mp_seg = mp.solutions.selfie_segmentation
segment = mp_seg.SelfieSegmentation(model_selection=1)

background = None
start_time = time.time()
fps_counter = FPSCounter()

print("Real-Time Human Invisibility System")
print("Developed by Vishesh Sharma")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    frame = cv2.resize(frame, (640, 480))  # 🔥 laptop safe

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break

    # Background capture
    if background is None:
        if time.time() - start_time > 4:
            background = frame.copy()
            print("Background captured")
        else:
            draw_text(frame, "Capturing Background...", (20, 40), 1)
            cv2.imshow("Invisible Human", frame)
            continue

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = segment.process(rgb)

    mask = result.segmentation_mask
    condition = mask > 0.6

    output = np.where(
        condition[..., None],
        background,
        frame
    )

    fps = fps_counter.update()
    draw_text(output, f"FPS: {fps}", (10, 40))
    draw_text(output, "Developed by Vishesh Sharma",
              (10, output.shape[0] - 20))

    cv2.imshow("Invisible Human (SAFE MODE)", output)

cap.release()
cv2.destroyAllWindows()
