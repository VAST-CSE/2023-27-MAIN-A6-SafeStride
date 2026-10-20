import cv2
import time
import threading
import queue
import pyttsx3
from ultralytics import YOLO

model = YOLO("yolov8n.pt")  # downloads automatically the first time
speech_queue = queue.Queue()


def speaker():
    while True:
        text = speech_queue.get()
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
        engine.stop()
        del engine

threading.Thread(target=speaker, daemon=True).start()

cap = cv2.VideoCapture(0)
last_spoken = {}   # label -> time it was last spoken
COOLDOWN = 5       # seconds before repeating the same object

while True:
    ok, frame = cap.read()
    if not ok:
        break

    result = model(frame, conf=0.5, verbose=False)[0]
    labels = sorted({model.names[int(c)] for c in result.boxes.cls})

    # draw boxes, then add a black caption bar underneath
    annotated = result.plot()
    caption = ", ".join(labels) if labels else "nothing detected"
    h, w = annotated.shape[:2]
    cv2.rectangle(annotated, (0, h - 40), (w, h), (0, 0, 0), -1)
    cv2.putText(annotated, caption, (10, h - 12),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)

    # speak only new objects, and not while it is already speaking
    now = time.time()
    new = [l for l in labels if now - last_spoken.get(l, 0) > COOLDOWN]
    if new and speech_queue.empty():
        for l in new:
            last_spoken[l] = now
        speech_queue.put("I can see " + ", ".join(new))

    cv2.imshow("Phase 1 - Object detection with voice (press q to quit)", annotated)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()