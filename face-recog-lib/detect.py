import face_recognition
import numpy
import cv2
# print(numpy.version.version)/

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if ret == False:
        continue

    gray_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    # image = cv2.imread("face-recog-lib/salmon.jpeg")
    # image = cv2.resize(image,(500,500))
    face_locations = face_recognition.face_locations(gray_frame)
    # print(face_locations)
    cv2.rectangle(frame,
                (face_locations[0][3],face_locations[0][0]),
                (face_locations[0][1],face_locations[0][2]),
                (0,0,255),
                3)
    cv2.imshow("Image",frame)
    
    key_pressed = cv2.waitKey(1) & 0xFF
    if key_pressed == ord('q'):
        break