import pdfplumber
from docx import Document


def extract_pdf(path: str):

    text = ""

    with pdfplumber.open(path) as pdf:

        for page in pdf.pages:

            page_text = page.extract_text()

            if page_text:

                text += page_text + "\n"

    return text


def extract_docx(path: str):

    document = Document(path)

    text = ""

    for paragraph in document.paragraphs:

        text += paragraph.text + "\n"

    return text


def extract_text(path: str):

    if path.lower().endswith(".pdf"):

        return extract_pdf(path)

    if path.lower().endswith(".docx"):

        return extract_docx(path)

    raise Exception("Unsupported file type.")
