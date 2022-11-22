import cv2
import time
import math
img = cv2.imread('1.png')
img_h, img_w, _ = img.shape
img = cv2.resize(img, (img_w//3, img_h//3))
cv2.imshow("img", img)
cv2.waitKey(0)

# Convert RGB format image to grayscale image
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("gray", gray)
cv2.waitKey(0)

# 二值化
ret, binary = cv2.threshold(gray, 125, 255, cv2.THRESH_BINARY)
cv2.imshow("binary", binary)
cv2.waitKey(0)

# 在二值化图像上检测轮廓
contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
ret_1, binary_1 = cv2.threshold(gray, 0, 0, cv2.THRESH_BINARY)
img1 = binary_1.copy()
cv2.drawContours(img1, contours, -1, (255, 255, 255), 2)
cv2.imshow("img1", img1)
cv2.waitKey(0)

# 根据轮廓特征（面积、周长等）剔除不满足要求的轮廓
ccontours = []
for c in contours:
    # k = cv2.arcLength(c,True) # 获取轮廓周长
    k = cv2.contourArea(c)  # 获取轮廓的面积
    if k > 100 and k < 100000:
        ccontours.append(c)
    # print(k)
img2 = binary_1.copy()
cv2.drawContours(img2, ccontours, -1, (255, 255, 255), 2)
cv2.imshow("img2", img2)
cv2.waitKey(0)

# 计算所有轮廓的最小包围盒
maxx = 0
maxy = 0
minx = 10000000
miny = 10000000
for c in ccontours:
    x, y, w, h = cv2.boundingRect(c)
    if (x < minx):
        minx = x
    if (x + w > maxx):
        maxx = x + w
    if (y < miny):
        miny = y
    if (y + h > maxy):
        maxy = y + h

# 绘制最小包围盒
#在img3上画外矩形
cv2.rectangle(img2, (minx, miny), (maxx, maxy), (255, 255, 255), 2)
cv2.imshow("img3", img2)
cv2.waitKey(0)

#在img上画外矩形
cv2.rectangle(img, (minx, miny), (maxx, maxy), (0, 0, 255), 2)
cv2.imshow("img", img)
cv2.waitKey(0)
