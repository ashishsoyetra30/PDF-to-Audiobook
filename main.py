import pyttsx3
import PyPDF2

book = open('python_tutorial.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)
speaker = pyttsx3.init() 

for num in range()
page = pdfReader.getPage(25)
text = page.extractText()
speaker.say(text)
speaker.runAndWait()