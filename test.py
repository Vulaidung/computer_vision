import cv2

cap = cv2.VideoCapture(2)

while True:
    ret, frame = cap.read()

    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV )
    
    mask = cv2inRange(hsvImage, )
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & OxFF == ord('q'):
        break


cap.release()

cv2.destroyAllWindows()

