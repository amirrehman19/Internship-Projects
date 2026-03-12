import cv2
from ultralytics import YOLO
import os
from datetime import datetime
import time

# Load YOLOv8 model
model = YOLO(r"C:\Users\amirr\Desktop\Ai-project\ppe detection\best.pt")

# Required PPE classes
REQUIRED_CLASSES = ["helmet", "vest", "gloves"]

# Directory for screenshots
screenshot_dir = r"C:\Users\amirr\Desktop\ppe detection\screenshots"
os.makedirs(screenshot_dir, exist_ok=True)

# Webcam setup
cap = cv2.VideoCapture(1)

if not cap.isOpened():
    print("Cannot open camera")
    exit()

# Screenshot counter
screenshot_counter = 1

# Timer
last_missing_ppe_time = 0
waiting_for_screenshot = False
missing_items_to_save = []

while True:
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    # YOLOv8 detection
    results = model.predict(frame, imgsz=640, conf=0.3)

    # Detected classes
    detected_classes = set([model.names[int(cls)] for cls in results[0].boxes.cls])

    # Missing PPE
    missing_items = [item for item in REQUIRED_CLASSES if item not in detected_classes]

    # Annotate
    current_time_str = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    annotated_frame = results[0].plot()
    cv2.putText(annotated_frame, f'Date & Time: {current_time_str}', (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

    # If new missing PPE found and not already waiting
    current_time = time.time()
    if missing_items and not waiting_for_screenshot:
        missing_items_to_save = missing_items
        last_missing_ppe_time = current_time
        waiting_for_screenshot = True
        print(f"Missing detected. Waiting 10 seconds before screenshot... Missing: {missing_items}")

    # If 10 seconds passed, take screenshot
    if waiting_for_screenshot and (current_time - last_missing_ppe_time >= 10):
        missing_str = ", ".join(missing_items_to_save)
        filename = f"object {screenshot_counter} ({missing_str} missing).png"
        filepath = os.path.join(screenshot_dir, filename)
        cv2.imwrite(filepath, annotated_frame)
        print(f"Screenshot saved after 10s: {filepath}")
        screenshot_counter += 1
        waiting_for_screenshot = False

    # Show webcam
    cv2.imshow('YOLOv8 PPE Detection', annotated_frame)

    # Quit on 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
