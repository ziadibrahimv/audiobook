import pyttsx3
import PyPDF2
book = open('parkangel.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages

speaker = pyttsx3.init()
for num in range(7, pages):
    page = pdfReader.getPage(1)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()
