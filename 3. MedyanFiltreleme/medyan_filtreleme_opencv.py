import cv2


image = cv2.imread(r"C:\Users\xxx\Documents\GitHub\Python-Goruntu-Isleme\MedyanFiltreleme\test.png")
#imread fonksiyonuyla goruntuluyu image değişkenine aktarıyoruz

image_blured = cv2.medianBlur(image,5)
#medianBlur fonksiyonuyla gürültüden temizliyoruz

cv2.imshow("Duzenlenmis resim",image_blured)
#resmi ekrana bastırıyoruz

cv2.imwrite(r"C:\Users\xxx\Documents\GitHub\Python-Goruntu-Isleme\MedyanFiltreleme\test_blured.png",image_blured)
#duzenlenmis resmi kaydediyoruz
