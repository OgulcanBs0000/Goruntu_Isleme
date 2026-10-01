# import cv2

# img = cv2.imread("image/gorsel.jpeg")

# print(img.shape)

# cv2.imshow("Orijinal", img)

# cv2.waitKey(0)
# cv2.destroyAllWindows()


# x2 yapma 

# import cv2

# img = cv2.imread("image/gorsel.jpeg")

# print("Orijinal:", img.shape)

# img_x2 = cv2.resize(img, None, fx=2, fy=2)

# print("x2:", img_x2.shape)

# cv2.imshow("Orijinal", img)
# cv2.imshow("x2", img_x2)

# cv2.waitKey(0)
# cv2.destroyAllWindows()

# x4 yapma 


# import cv2

# img = cv2.imread("image/gorsel.jpeg")

# print("Orijinal:", img.shape)

# # x2
# img_x2 = cv2.resize(img, None, fx=2, fy=2)
# print("x2:", img_x2.shape)

# # x4
# img_x4 = cv2.resize(img, None, fx=4, fy=4)
# print("x4:", img_x4.shape)

# cv2.imshow("Orijinal", img)
# cv2.imshow("x2", img_x2)
# cv2.imshow("x4", img_x4)

# cv2.waitKey(0)
# cv2.destroyAllWindows()



# x0.5 yapma 

# import cv2

# img = cv2.imread("image/gorsel.jpeg")

# print("Orijinal:", img.shape)

# # x2
# img_x2 = cv2.resize(img, None, fx=2, fy=2)
# print("x2:", img_x2.shape)

# # x4
# img_x4 = cv2.resize(img, None, fx=4, fy=4)
# print("x4:", img_x4.shape)

# x0.5
# img_x05 = cv2.resize(img, None, fx=0.5, fy=0.5)
# print("x0.5:", img_x05.shape)

# cv2.imshow("Orijinal", img)
# cv2.imshow("x2", img_x2)
# cv2.imshow("x4", img_x4)
# cv2.imshow("x0.5", img_x05)

# cv2.waitKey(0)
# cv2.destroyAllWindows()


# x0.25 yapma
import cv2

img = cv2.imread("image/gorsel.jpeg")

print("Orijinal:", img.shape)

# x2
img_x2 = cv2.resize(img, None, fx=2, fy=2)
print("x2:", img_x2.shape)

# x4
img_x4 = cv2.resize(img, None, fx=4, fy=4)
print("x4:", img_x4.shape)

# x0.5
img_x05 = cv2.resize(img, None, fx=0.5, fy=0.5)
print("x0.5:", img_x05.shape)

# x0.25
img_x025 = cv2.resize(img, None, fx=0.25, fy=0.25)
print("x0.25:", img_x025.shape)

cv2.imshow("Orijinal", img)
cv2.imshow("x2", img_x2)
cv2.imshow("x4", img_x4)
cv2.imshow("x0.5", img_x05)
cv2.imshow("x0.25", img_x025)

cv2.waitKey(0)
cv2.destroyAllWindows()

