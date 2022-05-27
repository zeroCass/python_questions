import numpy as np
import cv2
import pytesseract


def show_img(img, title='image'):
    cv2.imshow(title, img)
    cv2.waitKey(0)

def grayscale(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

def save_img(img, name):
    cv2.imwrite(name, img)


def inverted(img):
    return cv2.bitwise_not(img)

# deixar a img mais nitida, o ideal eh fornecer uma img cinza
def thresholding(gray_img, value_1, value_2, cv2_mehotd):
    thresh, im_bw = cv2.threshold(gray_img, value_1, value_2, cv2_mehotd)
    return im_bw


# noise img -> pixels que nao correspondem ao texto
def eliminate_noise():
    pass


def main():
    #pytesseract.pytesseract.tesseract_cmd = 'C:\\Users\\05694223101\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe'
    pytesseract.pytesseract.tesseract_cmd = 'C:\\Users\\zero\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe'
    ocr_result = []

    img = cv2.imread('images\lab_1.PNG')
    lab = cv2.imread('images\lab_1.PNG')

    img = cv2.resize(img, ((int(img.shape[1] * 1.2), int(img.shape[0] * 1.2))))
    lab = cv2.resize(lab, (int(lab.shape[1] * 1.2), int(lab.shape[0] * 1.2)))

    img = grayscale(img)
    show_img(img)

    img = cv2.GaussianBlur(img, (7, 7), 0)
    show_img(img)

    img = thresholding(img, 0, 230, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    show_img(img)

    #kernal = np.ones((3, 3), np.uint8)
    kernal = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 1))
    dilate = cv2.erode(img, kernal, iterations=1)
    #dilate = cv2.erode(img, kernal, iterations=1)
    img = dilate

    #img = cv2.dilate(img, cv2.getStructuringElement(cv2.MORPH_RECT, (3, 1)), iterations=1)


    print('DILATE')
    show_img(img)

    cnts = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]
    cnts = sorted(cnts, key=lambda x: cv2.boundingRect(x)[0])
    for count, c in enumerate(cnts):
        x, y, w, h = cv2.boundingRect(c)
        roi = lab[y:y+h, x:x+h]
        #save_img(roi, f'word_{count}.png')
        cv2.rectangle(lab, (x, y), (w+x, y+h), (36, 255, 12), 1)
        ocr_result .append(pytesseract.image_to_string(roi))
    show_img(lab)
    print(ocr_result)

if __name__ == '__main__':
    main()
