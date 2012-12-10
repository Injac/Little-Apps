from PIL import Image

im = Image.open("backgroundimage.jpg")
im.save("backgroundimage.bmp", "BMP")