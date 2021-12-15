import cv2

#upload tha face_haarcascade
face_Cascade = cv2.CascadeClassifier("assets/haarcascade_frontalface_default.xml")

#read the image
img = cv2.imread("photos/image12.jpg")

imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces = face_Cascade.detectMultiScale(imgGray,1.1,3)

#faces count
face_count = len(faces)


for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),3)
    cv2.putText(img,"Faces:"+str(face_count),(20,50),0,2,(25,0,0),3)
cv2.imshow("face",img)
cv2.waitKey(0)