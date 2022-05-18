import cv2  # 导入库
cap = cv2.VideoCapture(0)  # 开启摄像头

# 循环读取图像
while True:
    ok, img = cap.read()  # 读取摄像头图像
    if ok is False:
        print('无法读取到摄像头！')
        break

    # 展示图像
    cv2.imshow('image', img)

    k = cv2.waitKey(10)  # 键盘值
    if k == 27:   # 通过esc键退出摄像
        break

# 关闭摄像头
cap.release()
cv2.destroyAllWindows()
