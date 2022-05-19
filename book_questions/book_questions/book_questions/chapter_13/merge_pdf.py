import PyPDF2
import os

os.chdir(os.path.join(os.path.abspath('.'), 'book_questions\\automate_online-materials'))


try:
    with open('meetingminutes.pdf', 'rb') as file1, open('meetingminutes2.pdf', 'rb') as file2, \
        open('watermark.pdf', 'rb') as watermark:
        pdf1 = PyPDF2.PdfFileReader(file1)
        pdf2 = PyPDF2.PdfFileReader(file2)
        watermark_pdf = PyPDF2.PdfFileReader(watermark)
        merge_pdf = PyPDF2.PdfFileWriter()
        
        # get the first page of pdf2
        page_with_watermark = pdf2.getPage(0)
        # merge the first page of pdf2 with watermark page
        page_with_watermark.mergePage(watermark_pdf.getPage(0))


        # get page of the files
        # rotateClockwise - rotate the pages in degrees
        pages = [pdf1.getPage(0).rotateClockwise(180), pdf2.getPage(0)]
        for page in pages:
            merge_pdf.addPage(page)

        with open('mergepdf.pdf', 'wb') as output_file:    
            merge_pdf.write(output_file)

    
except Exception as e:
    print(e)