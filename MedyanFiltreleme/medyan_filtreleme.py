from PIL import Image

image  = Image.open(r"C:\Users\emre\Documents\GitHub\Python-Goruntu-Isleme\MedyanFiltreleme\test.png")

loader = image.load()

image_width,image_height= image.size[0],image.size[1]
graylist = [[0]*image_height for x in range(image_width)]

temparray=[[0]*(image_height+2) for x in range(image_width+2)]

for i in range(image.size[0]):
    for j in range(image.size[1]):
        r,g,b,_ = image.getpixel((i,j))
        gray = (int)((r*0.2126)+(g*0.7152)+(b*0.0722))
        graylist[i][j] = gray
        loader[i,j] = (gray,gray,gray)

for ni in range (1,image_width+1):
    for nj in range (1,image_height+1):
        temparray [ni] [nj]  =  graylist [ni-1] [nj-1]

med = [0]*9

gecici = 0

for m in range(1,image_width+1):

    for n in range (1,image_height+1):

        med[0] = temparray[m-1][n-1]

        med[1] = temparray[m-1][n]

        med[2] = temparray[m-1][n+1]

        med[3] = temparray[m][n-1]

        med[4] = temparray[m][n]

        med[5] = temparray[m][n+1]

        med[6] = temparray[m+1][n-1]

        med[7] = temparray[m+1][n]

        med[8] = temparray[m+1][n+1]

        med = sorted(med)

        value = med[4]

loader[m-1,n-1] = (value,value,value)

image.save(r"C:\Users\emre\Documents\GitHub\Python-Goruntu-Isleme\MedyanFiltreleme\resim_blured.png")
image.show
        
