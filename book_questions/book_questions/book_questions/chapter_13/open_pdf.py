import PyPDF2
import os

root = os.path.join(os.path.abspath('.'), 'book_questions\\automate_online-materials')
#print([file for file in os.listdir(root)])

try:
    
    pdf_obj = PyPDF2.PdfFileReader(open(os.path.join(root, 'meetingminutes.pdf'), 'rb'))
    print(f'Numbers of pages: {pdf_obj.numPages}')
    page_obj = pdf_obj.getPage(0)
    text = page_obj.extractText()
    print(text)
    

    # opening encrypted file
    with open(os.path.join(root, 'encrypted.pdf'), 'rb') as file:
        pdf_file = PyPDF2.PdfFileReader(file)
        if pdf_file.isEncrypted:
            print('The file is encrypted\nType the password: ')
            pwd = input()
            
            #assert pdf_file.decrypt(pwd),'Incorrent password'
            
            if pdf_file.decrypt(pwd):
                print('--The file was decrypt!--')
            else:
                print('Incorrent password')
        

except Exception as e:
    print(f'Error at opening file {e}')






