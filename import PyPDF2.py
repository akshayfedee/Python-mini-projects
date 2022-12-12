import PyPDF2
import pyttsx3

# Define the location of the PDF file
pdf_file_location = r'xxxxxxxlocation'

# Open the PDF file in read-binary mode
try:
    path = open(pdf_file_location, 'rb')
except FileNotFoundError:
    print("The PDF file could not be found at the specified location.")
    exit()

# Create a PdfFileReader object to read the PDF file
try:
    pdfreader = PyPDF2.PdfFileReader(path)
except PyPDF2.utils.PdfReadError:
    print("The PDF file could not be read.")
    exit()

# Retrieve the first page of the PDF file
frompage = pdfreader.getPage(0)

# Extract the text from the first page of the PDF file
text = frompage.extract_text(0)

# Initialize the pyttsx3 library with the default settings
speak = pytsx3.init(0)

# Speak the text that was extracted from the PDF file
speak.say(text)

# Run the text-to-speech engine and wait for it to finish speaking the text
speak.runAndWait()
