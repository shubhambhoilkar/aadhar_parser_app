# aadhar_parser_app

# Aadhaar Card OCR API with FastAPI

This project is a FastAPI-based web service that extracts Aadhaar card details using Tesseract OCR and stores the data in a MySQL database.

## Features

- Upload Aadhaar card images via API.
- Extract Name, Aadhaar Number, Date of Birth, Gender, and Address.
- Store extracted data in MySQL database.
- Validate and remove duplicate Aadhaar entries.
- JSON response for easy integration with frontend apps.

## Technologies Used

- Python 3.9+
- FastAPI
- Tesseract OCR (via pytesseract)
- OpenCV (for image preprocessing)
- SQLAlchemy (ORM)
- MySQL Database
- Uvicorn (for ASGI server)
