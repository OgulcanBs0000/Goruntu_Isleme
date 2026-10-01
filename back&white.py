import cv2

# Resmi oku
resim = cv2.imread("image/galatasaray.png")

# Siyah beyaz yap
gri_resim = cv2.cvtColor(resim, cv2.COLOR_BGR2GRAY)

# %25 boyutuna küçült
gri_kucuk = cv2.resize(gri_resim, None, fx=0.25, fy=0.25)

# Boyutları yazdır
print("Normal:", gri_resim.shape)
print("Kucuk:", gri_kucuk.shape)

# Göster
cv2.imshow("Siyah Beyaz Normal", gri_resim)
cv2.imshow("Siyah Beyaz Kucuk", gri_kucuk)

cv2.waitKey(0)
cv2.destroyAllWindows()