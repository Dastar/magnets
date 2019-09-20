from PIL import Image
from methods import add_frame


# b = Image.open('2.JPG')
# f = Image.open('1.png')
# #
# # b.show()
#
# im = Image.new(f.mode, f.size)
#
# w = 1200
# h = 800
# b = b.resize((w, h), Image.ANTIALIAS)
# # b.paste(f, (0, 0), f)
# im.paste(b, (0,0))
# im.paste(f, (0,0), f)
# im.show()

add_frame('1.png', '2.JPG')
