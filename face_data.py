import cv2
import numpy as np

cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

skip = 0
face_data = []
dataset_path = "face_data\\"

file_name = input("Enter your name")

while True:
    ret, frame = cap.read()

    if ret == False:
        continue

    gray_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray_frame,1.3,5)
    if len(faces) ==0:
        continue
    
    faces = sorted(faces,key = lambda x:x[2]*x[3],reverse=True)

    skip = skip + 1

    for face in faces[:1]:
        x,y,w,h = face
        offset = 10
        face_offset = frame[y-offset:y+h+offset,x-offset:x+w+offset].copy()
        face_offset = cv2.resize(face_offset,(100,100))
        if skip%20 == 0:
            face_data.append(face_offset)
            cv2.imwrite("face_data\images\\"+str(skip//20)+".jpg",face_offset)
        cv2.imshow("Face",face_offset)


    cv2.imshow("Video",gray_frame)

    key_pressed = cv2.waitKey(1) & 0xFF
    if key_pressed == ord('q'):
        break

face_data = np.array(face_data)
np.save(dataset_path+file_name,face_data)
print("Number of images =",face_data.shape[0])
cap.release()
cv2.destroyAllWindows()

