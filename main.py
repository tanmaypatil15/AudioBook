import pyttsx3
import PyPDF2
book = open('DBMS.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages

speaker = pyttsx3.init()
voices = speaker.getProperty('voices')
for voice in voices:
    print("Voice:")
    print(" - ID: %s" % voice.id)
    print(" - Name: %s" % voice.name)
    print(" - Languages: %s" % voice.languages)
    print(" - Gender: %s" % voice.gender)
    print(" - Age: %s" % voice.age)
rate = speaker.getProperty('rate')   # getting details of current speaking rate
print (rate)                        #printing current voice rate
speaker.setProperty('rate', 250)     # setting up new voice rate
voices = speaker.getProperty('voices')
speaker.setProperty('voice', voices[0].id)
for num in range(5, pages):
    page = pdfReader.getPage(num)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()
