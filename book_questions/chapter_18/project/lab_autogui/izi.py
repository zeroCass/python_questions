'''
 
 EH IMPORTANTE DESINSTALAR O CV2 E O USAR O QUE O MODULO EASYOCR INSTALLA
 EXISTE CONFLITO E A LIBRARY CV2 ESTA TOTALMENTE BUGADA

 ESOTU USANDO PIL NO LUGAR DO OPENCV, POIS ESTAVA CONFLITANDO COM OPENCV-HEADLESS
 O PIL EH MENOS OTIMIZADO E MENOS PODEROSO, MAS PARA ESSE PROPOSITO SERVIRA

'''

import easyocr
from PIL import Image, ImageDraw
import cv2
import sys
import numpy as np




lab_items = []

reader = easyocr.Reader(['pt'])

img = Image.open('images\lab_1.png')
img_r = img.resize((img.width * 2, img.height * 2))
img2arr = np.array(img_r)

result = reader.readtext(img2arr, detail=1, paragraph=False)


draw = ImageDraw.Draw(img)
print(result)
for (bbox, text, prob) in result:
    
    # Define bounding boxes - tl = topleft/br = bottonright
    # the values is divided by 2 cause the scale * 2
    (tl, _, br, _) = bbox
    tl = (int(tl[0] / 2), int(tl[1] / 2))
    br = (int(br[0] / 2), int(br[1] / 2))

    lab_items.append({'name': text, 'pos': [tl[0], tl[1]]})
    
    # Put rectangles and text on the image
    draw.rectangle((tl, br), outline='black')

# show the output image
img.show()
#img.save('rec_small.png')

for item in enumerate(lab_items):
    print(item)
