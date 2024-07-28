import face_recognition
import cv2
import numpy as np

video_capture = cv2.VideoCapture(0)

elon_image = face_recognition.load_image_file("face-recog-lib/elon_musk2.jpg")
elon_face_encoding = face_recognition.face_encodings(elon_image)[0]

kalam_image = face_recognition.load_image_file("face-recog-lib\kalam.jpg")
kalam_face_encoding = face_recognition.face_encodings(kalam_image)[0]

salmon_image = face_recognition.load_image_file("face-recog-lib\salmon.jpeg")
salmon_face_encoding = face_recognition.face_encodings(salmon_image)[0]

known_faces_encodings = [
elon_face_encoding,
kalam_face_encoding,
salmon_face_encoding
]

known_face_names = [
    "Elon Musk",
    "Abdul Kalam",
    "Salmon Joy"
]

face_location = []
face_encodings = []
process_this_frame = True

while True:
    ret, frame = video_capture.read()

    if process_this_frame == True:
        small_frame = cv2.resize(frame,(0,0),fx = 0.25,fy=0.25)
        rgb_small_frame = np.ascontiguousarray(small_frame[:,:,::-1])

        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame,face_locations)

        face_names = []
        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(known_faces_encodings,face_encoding)
            name = "Unknown"

            face_distances = face_recognition.face_distance(known_faces_encodings,face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]

            face_names.append(name)
    
    process_this_frame = not process_this_frame
    font = cv2.FONT_HERSHEY_DUPLEX
    print(name)
    cv2.putText(frame,name,(100,100),font,1.0,(0,0,0),1)

    cv2.imshow("Camera",frame)
    key_pressed = cv2.waitKey(1) & 0xFF
    if key_pressed == ord('q'):
        break