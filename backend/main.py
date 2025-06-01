from fastapi import FastAPI, File, Form, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os
import uuid

from backend.extractor import extract

app = FastAPI()

# Enable CORS (allow all origins and methods)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static files at /static
app.mount("/static", StaticFiles(directory="frontend"), name="static")

# Serve the index.html at root "/"
@app.get("/")
async def root():
    return FileResponse("frontend/index.html")


@app.post("/extract_from_doc")
def extract_from_doc(file_format: str = Form(...), file: UploadFile = File(...)):
    # Ensure uploads directory exists
    if not os.path.exists("uploads"):
        os.makedirs("uploads")

    contents = file.file.read()
    file_path = "uploads/" + str(uuid.uuid4()) + ".pdf"

    with open(file_path, "wb") as f:
        f.write(contents)

    try:
        data = extract(file_path, file_format)
    except Exception as e:
        data = {"error": str(e)}

    # Remove the uploaded file after processing
    if os.path.exists(file_path):
        os.remove(file_path)

    return data
