from fastapi import FastAPI, File, Form, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, HTMLResponse
import os
import uuid

from backend.extractor import extract

app = FastAPI()

# Enable CORS for all domains (frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static files (HTML/CSS)
app.mount("/static", StaticFiles(directory="frontend"), name="static")

# Serve the main HTML page
@app.get("/", response_class=HTMLResponse)
@app.head("/")  # Required for Render health check
async def root():
    return FileResponse("frontend/index.html")

# API endpoint to handle PDF uploads
@app.post("/extract_from_doc")
async def extract_from_doc(file_format: str = Form(...), file: UploadFile = File(...)):
    # Ensure uploads directory exists
    if not os.path.exists("uploads"):
        os.makedirs("uploads")

    contents = await file.read()
    file_path = "uploads/" + str(uuid.uuid4()) + ".pdf"

    with open(file_path, "wb") as f:
        f.write(contents)

    try:
        data = extract(file_path, file_format)
    except Exception as e:
        data = {"error": str(e)}

    # Clean up the uploaded file
    if os.path.exists(file_path):
        os.remove(file_path)

    return data
