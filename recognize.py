import cv2
faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
cap=cv2.VideoCapture(0)
cnt=0
Id=input("Enter id :")
while True:
    success,img=cap.read()
    if success:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces=faceCascade.detectMultiScale(gray,1.1,4)
        for (x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),3)
            cnt=cnt+1
            cv2.imwrite("dataset/ " + Id + "." +str(cnt) + ".jpg",gray[y:y + h, x:x + w])
            cv2.imshow("Face Detect",img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        elif cnt>11:
            break
cap.release()
cv2.destroyAllWindows()

