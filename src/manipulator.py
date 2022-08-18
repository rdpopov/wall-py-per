from PIL import Image
from itertools import repeat


def pad_image(img,pos: tuple,size: tuple,pad_col):
    ret = Image.new(mode="RGB",size=size,color=pad_col)
    ret.paste(img,pos)
    return ret
im = Image.open("../test.jpg")
color = im.load()[0, 0]
width, heigth = im.size
pos = (1920//2 - width//2, 1080//2 - heigth//2)

pad_image(im,pos,(1920,1080),color).save("../test_res.png",quality=95)
# so this fuking worked!!
