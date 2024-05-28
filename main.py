from PIL import Image
import numpy as np
dino = Image.open("F:\kimwo\python\picking_color_put_color\dino.jpg")
dinos = Image.open("F:\kimwo\python\picking_color_put_color\dino_change_color.jpg")
eye = Image.open("F:\kimwo\python\picking_color_put_color\eye.jpg")
mask = Image.open("F:\kimwo\python\picking_color_put_color\dino_mask.jpg").resize(dino.size).convert('L')
qrcode = Image.open("F:\kimwo\python\picking_color_put_color\\1mbJL.jpg")
width1, height1 = eye.size  #275 183
size = 100
def set_color (image, color):
    color +=(255,)
    width, height = image.size
    new_image = image.copy()
    for x in range(0,width):
        for y in range(0,height):
            if image.getpixel((x,y)) == (0,0,0):
                new_image.putpixel((x,y),color)
            elif image.getpixel((x,y)) == (255,255,255):
                new_image.putpixel((x,y), (255,255,255,255))
            else:
                new_image.putpixel((x,y), (255,255,255,255))
    return new_image
# dino_width, dino_height = dino.size
new_eye = eye.copy().resize((width1*20,height1*20))
new_width, new_height = new_eye.size
for x in range(0,new_width, size):
    for y in range(0,new_height,size):
        color = new_eye.getpixel((x,y))
        pixel_dino = set_color(qrcode, color).resize((size,size))
        new_eye.paste(pixel_dino,(x,y))
new_eye.save("mosaic_eye.jpg", dpi=(300,300))

# for x in range(0,width1, 10):
#     for y in range(0,height1, 10):
#         color = eye.getpixel((x,y))
#         dino_colored = set_color(dino, color)
#         if x+dino_width <=400 and y+dino_height <=400:
#             new_image.paste(dino_colored, (x,y))
#         else:
#             box = (0,0,min(dino_width, 400-x), min(dino_height, 400-y))
#             region = dino_colored.crop(box)
#             new_image.paste(region, (x,y))
# new_image.save("result.jpg")
        
# dinos.save('dino_change_color.jpg', 'JPEG')