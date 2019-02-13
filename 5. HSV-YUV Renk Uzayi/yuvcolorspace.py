from PIL import Image
import math

def  rgbtoyuv (R, G, B):
  r=R/255
  g=G/255 
  b=B/255

  Y=(0.299*r)+(0.587*g)+(0.114*b)
  U=0.492*(b-Y)
  V=0.877*(r-Y)

  return int(Y*255),int(U*255),int(V*255) 

resim=Image.open("ornek.jpg").convert("RGB")
resim_pix = resim.load()
w=resim.size[0]
hg=resim.size[1]
for i in range(w):
  for j in range(hg):
      r, g, b = resim.getpixel((i, j))
      h, s, v = rgbtoyuv(r, g, b)
      resim_pix[i,j] = (h, s, v)
resim.save("imageyuv.jpg")
resim.show()
