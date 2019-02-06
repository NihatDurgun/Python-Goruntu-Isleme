
import cv2
#İlk olarak opencv kütüphanesini projemize dahil ediyoruz

resim = cv2.imread(r"C:\Users\abc\Desktop\abc\test.png")
#'imread' adlı fonksiyonuyla duzenliyecegimiz resmi 'resim' adlı degiskene atıyoruz 

resim_gri = cv2.cvtColor(resim,cv2.COLOR_BGR2GRAY)
#'cvtColor' adlı fonksiyonla resmi griye çevirip 'resim_gri' adlı degiskenimize atıyoruz

cv2.imwrite(r"C:\Users\abc\Desktop\abc\test_yeni.png",resim_gri)
#duzenlenen resmi 'imwrite' fonksiyonuyla kaydediyoruz.


cv2.imshow("Orjinal Resim",resim)
#orjinal resmi 'imshow' fonksiyonuyla goruntuluyoruz
cv2.imshow("Duzenlemis Resim",resim_gri)
#duzenledigimiz resmi goruntuluyoruz
