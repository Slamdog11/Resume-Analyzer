from PyPDF2 import PdfReader

def extract_text(pdf_file):
    text = ""

    pdf = PdfReader(pdf_file)

    for page in pdf.pages:
        text += page.extract_text()

    return text