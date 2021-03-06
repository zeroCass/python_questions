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
from PIL import Image, ImageDraw, ImageFont



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



def resize_img(img:Image, SQUARE_FIT_SIZE) -> Image:
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

        print(f'{img.filename} was resized.')
        return img.resize((width, height))
    return img



def addlogo(img:Image, filename:str, img_logo:Image):
    '''
        add logo in the lower left corner of the image 
    '''

    source_w, source_h = img.size
    logo_w, logo_h = img_logo.size
    img.paste(img_logo, box=(source_w - logo_w, source_h - logo_h), mask=img_logo)
    print(f'logo has been added in {filename}.')


def addtext(img:Image, text:str, text_color:str='black', font:str='arial', rectangle:bool=False):
    '''
        Adds a text to img 
        if the rectangle is True, add the rect

        futere features: it is possible to calculate the lenght of the
        rectangle based on the lenght of the text
    '''


    # creates the obj to draw passing the img that will be used for draw
    draw_text = ImageDraw.Draw(img)
    
    # this is one the approchs to draw, but the size is not chosen
    #draw_text.text((20, 150), text, fill='red')

    # crates the font obj passing the font name and the size of the font
    _font = ImageFont.truetype(font + '.ttf', 16)
    # the second approch to draw
    draw_text.text((10, 10), text, fill=text_color, font=_font)

    if rectangle:
        draw_text.rectangle((6,10,70,27), outline='black')

    print('Text added with sucess.')




# the current dir is the img_folder
def main():
    #copy_img(10)
    
    # create the folder for the img with logo
    os.makedirs('with_logo', exist_ok=True)

    img_logo = Image.open(LOGO_FILE_NAME)
    # resize the logo
    img_logo = resize_img(img_logo, 100)

    for filename in os.listdir():
        if (filename.lower().endswith('png') or filename.lower().endswith('jpg')) \
                and filename != LOGO_FILE_NAME:

            img = Image.open(filename)
            img_name = img.filename

            # resize the img
            img = resize_img(img, SQUARE_FIT_SIZE)
            # add the logo in the img resized
            
            addlogo(img, filename, img_logo)
            # save the img in the folder withlogo
            
            # add the text and the rectangle
            addtext(img, text='The cat', rectangle=True)

            img_name = img_name.replace('.png', '_wlogo.png')
            img.save(os.path.join('with_logo', img_name))
    




if __name__ == '__main__':
    main()
