import cv2
from ultralytics import YOLO

# Load your YOLOv8 model (Escape the backslashes properly OR use a raw string with 'r' prefix)
model = YOLO(r"C:\Users\amirr\Desktop\ppe detection\best.pt")  

# Start capturing webcam feed
cap = cv2.VideoCapture(0)  # 0 is the default webcam

if not cap.isOpened():
    print("Cannot open camera")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    # Run YOLOv8 prediction on the frame
    results = model.predict(frame, imgsz=640, conf=0.35)

    # Visualize results on the frame
    annotated_frame = results[0].plot()

    # Display the frame
    cv2.imshow('YOLOv8 Webcam Detection', annotated_frame)

    # Exit loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
