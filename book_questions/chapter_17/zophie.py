import os
from PIL import Image

os.chdir(os.path.dirname(os.path.abspath(__file__)))
os.chdir('..\\automate_online_materials')

# open a image file as obj
cat = Image.open('zophie.png')
print(cat.size, cat.format_description, cat.filename)

# save the new image
cat.save('zhopie.jpg')

# create a new image -> agrg: color mode, (with-height), color
new_image = Image.new('RGBA', (100, 200), 'red')
new_image.save('red_image.png')

# crop retorns a image obj cropped
cropped_cat = cat.crop((335, 345, 565, 560))
cropped_cat.save('cropped_zophie.png')

# copy returns the same image but in different obj
cat_copy = cat.copy()
# paste() -> paste a imgame at cordinate over a image
cat_copy.paste(cropped_cat,(0, 0))
cat_copy.save('zhopie_pasted.png')

img_width, img_height = cat.size
face_width, face_height = cropped_cat.size
face_cat = Image.new('RGBA', (img_width, img_height))
for left in range(0, img_width, face_width):
    for top in range(0, img_height, face_height):
        print(left, top)
        face_cat.paste(cropped_cat,(left, top))
face_cat.save('face_cat.png')

# rotate image
face_cat_rotate = face_cat.copy()
face_cat_rotate.rotate(6).save('face_cat_rotate.png')
face_cat_rotate.rotate(6, expand=True).save('face_cat_rotate_expand.png')


# is possible to get pixels and putpixels into cordinate (x, y)
# Image.getpixcel(x, y)
# Image.putpixel(x, y, (RGBA))








