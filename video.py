import cv2
cap = cv2.VideoCapture(0)
img = cv2.imread("cv2-logo.jpeg")

while True:
    ret, frame = cap.read()
     

    if ret == False:
        continue
    
    img = cv2.resize(img,(frame.shape[1],frame.shape[0]))
    # print(frame.shape,img.shape)
    new_img = cv2.addWeighted(frame,0.8,img,0.2,0)
    # cv2.circle(frame,(frame.shape[1]//2,frame.shape[0]//2),50,(255,0,0),-1)
    cv2.imshow("Video",new_img)

    key_pressed = cv2.waitKey(1) & 0xFF

    if key_pressed == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
