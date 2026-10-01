import cv2
import matplotlib.pyplot as plt

# Resmi oku
resim = cv2.imread("image/image1.jpeg")

if resim is None:
    print("Resim bulunamadi!")
    exit()

# Gri tona cevir
gri = cv2.cvtColor(resim, cv2.COLOR_BGR2GRAY)

# Yukseklik ve genislik
h, w = gri.shape

print("Genislik:", w)
print("Yukseklik:", h)

# Orta noktalar
orta_x = w // 2
orta_y = h // 2

# 4 parcaya ayir
parca1 = gri[0:orta_y, 0:orta_x]
parca2 = gri[0:orta_y, orta_x:w]
parca3 = gri[orta_y:h, 0:orta_x]
parca4 = gri[orta_y:h, orta_x:w]

# Parcalari goster
cv2.imshow("1 - Sol Ust", parca1)
cv2.imshow("2 - Sag Ust", parca2)
cv2.imshow("3 - Sol Alt", parca3)
cv2.imshow("4 - Sag Alt", parca4)

cv2.waitKey(0)
cv2.destroyAllWindows()


# Her parçanın histogramını hesapla
hist1 = cv2.calcHist([parca1], [0], None, [256], [0, 256])
hist2 = cv2.calcHist([parca2], [0], None, [256], [0, 256])
hist3 = cv2.calcHist([parca3], [0], None, [256], [0, 256])
hist4 = cv2.calcHist([parca4], [0], None, [256], [0, 256])

# Histogramları göster
plt.plot(hist1, label="Parca 1")
plt.plot(hist2, label="Parca 2")
plt.plot(hist3, label="Parca 3")
plt.plot(hist4, label="Parca 4")

plt.xlabel("Parlaklik Seviyesi")
plt.ylabel("Piksel Sayisi")
plt.title("4 Parcanin Histogramlari")
plt.legend()

plt.show()

# 4 histogrami topla
ana_histogram = hist1 + hist2 + hist3 + hist4

# Ana histogrami goster
plt.figure()

plt.plot(ana_histogram)

plt.xlabel("Parlaklik Seviyesi")
plt.ylabel("Toplam Piksel Sayisi")
plt.title("Ana Histogram")

plt.show()