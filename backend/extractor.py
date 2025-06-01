from pdf2image import convert_from_path
import pytesseract
import backend.util as util

from backend.parser_prescription import PrescriptionParser
from backend.parser_patient_details import PatientDetailsParser

# Use Linux paths for Render/Docker deployment
POPPLER_PATH = "/usr/bin"
pytesseract.pytesseract.tesseract_cmd = "/usr/bin/tesseract"

def extract(file_path, file_format):
    pages = convert_from_path(file_path, poppler_path=POPPLER_PATH)
    document_text = ''

    if pages:
        page = pages[0]
        processed_image = util.preprocess_image(page)
        text = pytesseract.image_to_string(processed_image, lang='eng')
        document_text = '\n' + text

    if file_format == 'prescription':
        extracted_data = PrescriptionParser(document_text).parse()
    elif file_format == 'patient_details':
        extracted_data = PatientDetailsParser(document_text).parse()
    else:
        raise Exception(f"Invalid document format: {file_format}")

    return extracted_data
