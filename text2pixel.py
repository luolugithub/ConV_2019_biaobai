from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

ShowText = '计算所加油，武汉加油，中国加油!!'

font = ImageFont.truetype('Zpix.ttf', 15)  # load the font
size = font.getsize(ShowText)  # calc the size of text in pixels
image = Image.new('1', size, 1)  # create a b/w image
draw = ImageDraw.Draw(image)
draw.text((0, 0), ShowText, font=font)  # render the text to the bitmap


def mapBitToChar(im, col, row):
    if im.getpixel((col, row)):
        return ' '
    else:
        return '#'


for r in range(size[1]):
    print(''.join([mapBitToChar(image, c, r) for c in range(size[0])]))
