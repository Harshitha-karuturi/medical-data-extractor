# 🩺 Medical Data Extraction using Python, OCR, FastAPI & HTML

This project extracts structured data such as patient name, diagnosis, medicines, and directions from medical PDF files like prescriptions and patient forms. It uses OCR (Optical Character Recognition) to process scanned PDFs and provides a simple web frontend for easy uploads. The output here is in tabluar format.

## 🚀 Features

* 📄 Upload medical PDF files
* 🧠 OCR with Tesseract to extract text
* 🧪 Image preprocessing with OpenCV
* 🧾 Text parsing using regex
* ⚙️ FastAPI-based backend
* 🌐 HTML + CSS frontend interface
* 📊 Output displayed in clean table format


## 🛠️ Tech Stack

* **Backend**: Python, FastAPI, Tesseract OCR, OpenCV, pdf2image
* **Frontend**: HTML, CSS, JavaScript
* **Other Tools**: Poppler for PDF rendering


## 📁 Project Structure

medical_data_extractor/
│
├── backend/                         # Backend logic and OCR
│   ├── main.py                      # FastAPI server
│   ├── extractor.py                 # Handles OCR + parsing
│   ├── parser_generic.py            # Base class for document parsers
│   ├── parser_prescription.py       # Parser for prescriptions
│   ├── parser_patient_details.py    # Parser for patient details
│   ├── util.py                      # Image preprocessing logic
│   └── __init__.py
│
├── frontend/                        # Web frontend
│   ├── index.html                   # Main upload form
│   └── css/
│       └── style.css                # Styles for frontend
│
├── resources/                       # Sample PDFs
│   ├── prescription/pre_1.pdf
│   └── patient_details/pat_1.pdf
│
├── uploads/                         # Temporary storage for uploaded files
│
├── requirements.txt                 # Python dependencies
├── README.md                        # Project documentation
└── venv/                            # Virtual environment (optional)



## ⚙️ Setup Instructions

### 1. 📦 Install Python Packages

pip install -r requirements.txt

### 2. 🔧 Install External Tools

| Tool          | Purpose      | Install Link                                                                                 |
| ------------- | ------------ | -------------------------------------------------------------------------------------------- |
| Tesseract OCR | Image → Text |(https://github.com/tesseract-ocr/tesseract)     |
| Poppler       | PDF → Image  |(https://blog.alivate.com.au/poppler-windows/) |

Update paths in `extractor.py`:

POPPLER_PATH = r"C:\\path\\to\\poppler\\bin"
pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"


### 3. ▶️ Run the Backend Server

uvicorn backend.main:app --reload

FastAPI server runs at: (http://127.0.0.1:8000/)



### 4. 🌐 Open Frontend

Simply visit:

http://127.0.0.1:8000/

* Choose a file type (`prescription` or `patient_details`)
* Upload a PDF
* Click **Extract Data**
* View the output below in a table



## 📋 Output Example (Table format shown on frontend)

| Field            | Value                             |
| ---------------- | --------------------------------- |
| patient_name    | Marta Sharapova                   |
| patient_address | 9 tennis court, new Russia, DC    |
| medicines        | Prednisone 20 mg, Lialda 2.4 gram |
| directions       | Take once daily with food         |
| refills          | 3                                 |


## 💡 Future Enhancements

* Add CSV/Excel download of extracted data
* Handle handwritten text with advanced OCR models


## 👩‍💻 Author

**Karuturi Harshitha Devi**

#   m e d i c a l - d a t a - e x t r a c t o r  
 