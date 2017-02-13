from PIL import Image

with open('abc.txt','r') as f:
    pixels = eval(f.read())
'''
coloredPixels = []
for px in pixels:
    if px != (255,255,255):
        print(px)
        coloredPixels.append(px)
'''

im = Image.new("RGB", (929, 569))
im.putdata(pixels)
im.show()
