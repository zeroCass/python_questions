'''
 
 EH IMPORTANTE DESINSTALAR O CV2 E O USAR O QUE O MODULO EASYOCR INSTALLA
 EXISTE CONFLITO E A LIBRARY CV2 ESTA TOTALMENTE BUGADA

'''

import easyocr
from PIL import Image, ImageDraw
import cv2
#import matplotlib.pyplot as plt

reader = easyocr.Reader(['pt'])
img = cv2.imread('lab_1.png')
img = cv2.resize(img, ((int(img.shape[1] * 2), int(img.shape[0] * 2))))
imgpil = Image.open('lab_1.png')
imgpil = imgpil.resize((imgpil.width * 2, imgpil.height * 2))

result = reader.readtext(img, detail=1, paragraph=False)
print(result)
draw = ImageDraw.Draw(imgpil)
for (bbox, text, prob) in result:
    
    #Define bounding boxes
    (tl, tr, br, bl) = bbox
    tl = (int(tl[0]), int(tl[1]))
    tr = (int(tr[0]), int(tr[1]))
    br = (int(br[0]), int(br[1]))
    bl = (int(bl[0]), int(bl[1]))
    
   
    #Put rectangles and text on the image
    #cv2.rectangle(img, tl, br, (0, 255, 0), 2)
    draw.rectangle((tl, br), outline='black')

# show the output image
#cv2.imshow("Image", img)
#cv2.waitKey(0)
imgpil.save('rec.png')
