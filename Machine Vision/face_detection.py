import cv2
import serial
import time


serial_port = 'COM9'
baud_rate = 115200
ser = serial.Serial(serial_port, baud_rate)
time.sleep(2)


cascade_path = 'src\Machine Vision\haarcascade_frontalface_default.xml'
face_cascade = cv2.CascadeClassifier(cascade_path)


if face_cascade.empty():
    raise IOError("Failed to load cascade classifier")


cap = cv2.VideoCapture(1)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=5,
        minSize=(30, 30)
    )

    for (x, y, w, h) in faces:
        global center_x, center_y
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        center_x = x + w // 2
        center_y = y + h // 2

        cv2.circle(frame, (center_x, center_y), 5, (255, 0, 0), -1)

        cv2.putText(frame, f"({center_x}, {center_y})", (center_x - 20, center_y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 1)

        if len(faces) != 0:

            ser.write(f"{center_x},{center_y}\n".encode())
            print(f"X = {center_x}, Y = {center_y}")

    cv2.imshow('Detection', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
ser.close()
