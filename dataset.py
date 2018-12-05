import cv2
import numpy as np

import sqlite3

faceDetect=cv2.CascadeClassifier('face-detect.xml');
cam=cv2.VideoCapture(0);

def insertOrUpdate(Id,Name):
    conn=sqlite3.connect("cv.db")
    cmd="SELECT * FROM wajah WHERE ID="+str(Id)
    cursor=conn.execute(cmd)
    isRecordExist=0
    for row in cursor:
        isRecordExist=1
    if(isRecordExist==1):
        cmd="UPDATE wajah SET Name="+str(Name)+"WHERE ID="+str(Id)
    else:
        cmd="INSERT INTO wajah(Id,Name)Values("+str(Id)+",'"+str(Name)+"')"
        conn.execute(cmd)
    conn.commit()
    conn.close()

id=raw_input('Enter User id')
name=raw_input('Enter User name')
insertOrUpdate(id,name)
sampleNum=0
while(True):
    ret,img=cam.read();
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    face= faceDetect.detectMultiScale(gray, 1.3,5,);
    for(x,y,w,h) in face:
        sampleNum=sampleNum+1;
        cv2.imwrite("dataset/user"+str(id)+"."+str(sampleNum)+".jpg",gray[y:y+h,x:x+w])
        cv2.rectangle(img,(x-50,y-50),(x+w+50,y+h+50),(0,255,0),2)
        cv2.waitKey(100);
    cv2.imshow("Face",img);
    cv2.waitKey(100);
    if(sampleNum>20):
        break;
cam.release()
cv2.destroyAllWindows()