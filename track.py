from ultralytics import YOLO
import cv2

model = YOLO("yolov8s.pt")

cap = cv2.VideoCapture(1)

while True:
    ret, frame = cap.read()

    if not ret:
        print("No frame")
        break

    results = model(frame)

    detected = set()

    for box in results[0].boxes:
        cls = int(box.cls[0])
        detected.add(model.names[cls])

    if detected:
        print("Detected:", ", ".join(detected))
    frame = results[0].plot()

    cv2.imshow("Phone Object Detection", frame)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()