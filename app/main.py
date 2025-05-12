from fastapi import FastAPI, Request, UploadFile, File, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import shutil
import os
from datetime import datetime
from app.ocr import extract_text
from app.nlp import extract_aadhar_data , extract_address
from app.db import insert_user_data

app =FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR ,exist_ok=True)

@app.get("/",response_class=HTMLResponse)
async def from_page(request: Request):
    return templates.TemplateResponse("upload.html",{"response":request})

@app.post("/upload")
async def upload_file(request: Request, file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    text = extract_text(file_path)
    data = extract_aadhar_data(text)
    data["address"] = extract_address(text)

    try:
        dob = datetime.strptime(data[dob],"%d/%m/%Y").date()
    except:
        dob = None

    insert_user_data(data["name"], dob, data["aadhar"], file.filename)
    return templates.TemplateResponse("result.html",{"request":request,"data":data})
