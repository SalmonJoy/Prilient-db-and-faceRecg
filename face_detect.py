import cv2
import numpy as np

cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

saved = 0
while True:
    ret, frame = cap.read()

    if ret == False:
        continue

    gray_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray_frame,1.3,5)
    if len(faces) == 0:
        continue

    for face in faces[:1]:
        x,y,w,h = face
        # print(x,y,w,h)
        offset = 10
        # cv2.rectangle(frame,(x-offset,y-offset),(x+w+offset,y+h+offset),(0,0,255),2)
        cv2.imshow("Face",frame[y-offset:y+h+offset,x-offset:x+h+offset])
        face_image = frame[y-offset:y+h+offset,x-offset:x+h+offset].copy()
        face_image = cv2.resize(face_image,(120,120))
        if saved < 10:
            cv2.imwrite("face"+str(saved)+".jpg",face_image)
            saved = saved + 1


    cv2.imshow("Video",frame)

    key_pressed = cv2.waitKey(1) & 0xFF
    if key_pressed == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()