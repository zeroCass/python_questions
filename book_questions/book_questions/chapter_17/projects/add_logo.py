'''
Projeto: Adicionando um logo

Suponha que você tenha a tarefa maçante de redimensionar milhares de
imagens e adicionar um pequeno logo como marca-dágua no canto de cada
uma delas. Fazer isso com um programa gráfico básico como o Paintbrush ou
o Paint demoraria muito. Uma aplicação gráfica mais sofisticada como o
Photoshop pode fazer processamento em batch (lote), porém esse software
custa centenas de dólares. Vamos criar um script para fazer isso.

'''


import os
from pickle import NONE
from PIL import Image, ImageDraw



# get the img folder
img_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'img_folder')
os.chdir(img_folder)


SQUARE_FIT_SIZE = 300 # to resize
LOGO_FILE_NAME = 'catlogo.png'  # this file need exists in img_folder



def copy_img(count:int = 1) -> None:
    '''
        recive a count of how img will copy from automate folder
        to projects/img_folder
    '''

    # this join the file folder with the previous 3 folder and then the automate folder
    materials_folder = os.path.abspath(
            os.path.join(__file__, '../../..//automate_online_materials'))
    
    source_img = Image.open(os.path.join(materials_folder, 'zophie.png'))
    img_name = source_img.filename.split('\\')[-1].replace('.png', '')

    for x in range(0, count):
        copy = source_img.copy()
        copy = copy.save(os.path.join(img_folder, f'zhopie_{x}.png'))
        print(f'Image {img_name}_{x} was copied.')


def addlogo(img: Image, logo: Image) -> Image:
    '''
        add a logo e return the new img with logo
    '''



def resize_img(img: Image, SQUARE_FIT_SIZE) -> Image:
    '''
        Resize the img based on SQUARE_FIT_SIZE value
        the proportion is maintained
        returns Image if sucess, otherwise returns None
    '''
    width, height = img.size
    if width > SQUARE_FIT_SIZE and height > SQUARE_FIT_SIZE:
        if width > height:
            height = int((SQUARE_FIT_SIZE * height) / width)
            width = SQUARE_FIT_SIZE
        else:
            width = int((SQUARE_FIT_SIZE * width) / height)
            height = SQUARE_FIT_SIZE

        return img.resize((width, height))
    return None

def add_logo(img: Image):
    pass



def main():
    #copy_img(10)

    for filename in os.listdir():
        if filename.lower().endswith('png') or filename.lower().endswith('jpg') \
                and filename != LOGO_FILE_NAME:
            img = Image.open(filename)
            img_name = img.filename
            img = resize_img(img, SQUARE_FIT_SIZE)
            if img:
                # img_name = img_name.replace('.png', '') + '_resized.png'
                # img.save(img_name)
                print(f'{img_name} was resized') 
            addlogo(img, img_logo)

if __name__ == '__main__':
    main()
