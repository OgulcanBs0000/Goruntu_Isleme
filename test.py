import cv2

resim = cv2.imread("image/galatasaray.png")

yeni_resim = cv2.resize(resim, (400, 500))

cv2.imshow("Galatasaray", yeni_resim)

cv2.waitKey(0)
cv2.destroyAllWindows()