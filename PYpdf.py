# setup.py

# from PyPDF2 import PdfFileReader

# def extract_info(pdf_path):
#     with open(pdf_path, 'rb') as f:
#         pdf = PdfFileReader(f)
#         information = pdf.getDocumentInfo()
#         number_of_pages = pdf.getNumPages()
    
#     txt = f"""
#     Information about {pdf_path}:
    
#     Title: {information.title}
#     Number of pagers: {number_of_pages}
#     """
#     page = pdf.getPage(0)
#     print(txt)
#     print(information)
#     print(page.extractText())
    
# if __name__ == '__main__':
#     path = 'test.pdf'
#     extract_info(path)
import re
from PyPDF2 import PdfFileReader
temp = open('test.pdf', 'rb')
PDF_read = PdfFileReader(temp)
first_page = PDF_read.getPage(0)
textFile = first_page.extractText()
print(textFile)

#find all uppercase words
regex = re.findall(r"\b[A-Z][A-Z]+\b", textFile)
print(regex)


