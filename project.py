import cv2
from ultralytics import YOLO

model = YOLO('best.pt')  

cap = cv2.VideoCapture(1)

if not cap.isOpened():
    print("Error: Unable to access the camera.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Unable to capture video.")
        break

    results = model(frame)

    annotated_frame = results[0].plot()

    cv2.imshow('YOLOv8 Inference', annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
