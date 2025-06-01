from pdf2image import convert_from_path
import pytesseract
import backend.util as util
import os

from backend.parser_prescription import PrescriptionParser
from backend.parser_patient_details import PatientDetailsParser

# Dynamically set paths based on the operating system
POPPLER_PATH = None
if os.name == 'nt':  # Windows
    POPPLER_PATH = r'C:\poppler\Library\bin'
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
else:  # Linux (e.g., Render deployment)
    POPPLER_PATH = None  # poppler-utils is installed system-wide in Docker
    pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'  # or just leave default

def extract(file_path, file_format):
    try:
        # Convert first page of PDF to image
        pages = convert_from_path(file_path, poppler_path=POPPLER_PATH)
        document_text = ''

        if pages:
            page = pages[0]
            processed_image = util.preprocess_image(page)
            text = pytesseract.image_to_string(processed_image, lang='eng')
            document_text = text.strip()
            print("OCR text:\n",document_text)

        # Parse based on format
        if file_format == 'prescription':
            return PrescriptionParser(document_text).parse()
        elif file_format == 'patient_details':
            return PatientDetailsParser(document_text).parse()
        else:
            raise Exception(f"Invalid document format: {file_format}")
    except Exception as e:
        return {"error": str(e)}
