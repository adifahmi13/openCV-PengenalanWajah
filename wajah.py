import cv2
import sqlite3

videoCam = cv2.VideoCapture(0)

face = cv2.CascadeClassifier('face-detect.xml')

while True:
    cond, frame = videoCam.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    wajah = face.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in wajah:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 0), 5)


    cv2.imshow('Face ++ detection', frame)

    k = cv2.waitKey(1) & 0xff
    if k == ord('q'):
        break

videoCam.release()
cv2.destroyAllWindows()