import cv2

if __name__ == "__main__":

    #加载训练好的人脸检测器
    faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')

    #打开摄像头
    cap = cv2.VideoCapture(0)
    frep = cv2.getTickFrequency() #系统频率
    while True:

        #读取一帧图像
        succes,img = cap.read()

        t1 = cv2.getTickCount()
        #转换为灰度
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

        #进行人脸检测
        faces = faceCascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5,minSize=(50,50),flags=cv2.CASCADE_SCALE_IMAGE)

        #画框
        for (x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),3)

        t2 = cv2.getTickCount()

        fps = freq/(t2-t1)
        #显示速度
        cv2.putText(img,'FPS: %.2f'%(fps),(0,15), cv2.FONT_HERSHEY_SIMPLEX,0.5(0,0,255))

        #显示检测结果
        cv2.imshow("FACE",img)
        #按q退出
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
cap.release()
