#install pyDF2
pip install PyPDF2

#importing all the required modules
import PyPDF2

#creating an object
file = open('example.pdf', 'rb')

#createing a pdf reader object
fileReader = PyDF2.PdfFileReader(file)

#print the numer of pages in pdf file
print(fileReader.numPages)
