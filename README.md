# Medical Data Extraction

Mediscan is an Optical Character Recognition (OCR)-driven solution engineered for the automated and accurate extraction of patient and prescription metadata from digital PDF documents.

## <a name="a1">1. What is OCR?</a>

OCR, or Optical Character Recognition, is basically a smart digital eye. Its job is simple: to take pictures of text—whether that's a scanned paper, a tricky PDF, or a photo you snapped—and turn it into text that you can actually edit, search for, and copy-paste. It changes a static picture of words into live, machine-usable data.

The reason modern OCR works so well is Machine Learning (ML). ML uses algorithms (like deep learning networks) that are trained on massive libraries of text to recognize characters instantly. Even better, it uses language models to understand context. So if a character could look like an 'L' or a '1', the AI checks the surrounding words to figure out which one makes sense. This means OCR systems are constantly learning and getting better, especially with tricky handwriting or domain-specific lingo.

This project leverages OCR to transform healthcare documents into clean, machine-readable data.


## <a name="a2">2. Introduction to Project</a>

Whenever a patient visits a hospital, multiple documents such as medical records, prescriptions, and reports are generated. These records are essential for maintaining medical history, processing insurance claims, and ensuring continuity of care.

However, manually processing thousands of such documents is time-consuming, error-prone, and labor-intensive. MediScan automates this process using OCR technology to extract key information efficiently.

Supported Document Types(pdf):

1. Patient Medical Record

2. Prescription

The system extracts structured fields like patient details, contact information, medications, dosage instructions, and more.

## <a name="a3">3. Project Execution Workflow</a>

**Step 1**: Convert PDF to image using pdf2image
**Step 2**: Preprocess image using OpenCV (adaptive thresholding and binarization)
**Step 3**: Extract text from the image using Tesseract OCR
**Step 4**: Parse and filter useful information using Regular Expressions (RegEx) and return as JSON
**Step 5**: Serve the results through a FastAPI backend server that accepts PDF uploads and returns structured JSON data
**Step 6**: Build a Streamlit frontend to interact with the backend, visualize extracted results, and optionally save them to the database

## <a name="a5">5. What did I learn through this project?</a>

-Implemented OCR-based document processing with Tesseract and OpenCV
-Enhanced Python coding practices with Object-Oriented Programming and modular design
-Built and deployed a FastAPI backend server
-Performed unit testing using pytest
-Learned API testing using Postman
-Connected a Streamlit frontend to a FastAPI backend using the requests library

## <a name="a6">6. Challenges faced during this project</a>

-Fine-tuning parameters for adaptive thresholding took multiple trial-and-error iterations
-Integrating Streamlit with FastAPI (especially for file uploads) had limited online resources
-Managing multiple Python environments and package dependencies

## <a name="a7">7. Directory Structure of Project</a>

```
Medi-Scan
│   .gitignore
│   README.md
│   requirements.txt
│
├───backend
│   │
│   ├───resources
│   │   ├───patient_details
│   │   │       pd_1.pdf
│   │   │       pd_2.pdf
│   │   │
│   │   └───prescription
│   │           pre_1.pdf
│   │           pre_2.pdf
│   │
│   ├───src
│   │       extractor.py
│   │       main.py              # FastAPI backend server
│   │       parser_generic.py
│   │       parser_patient_details.py
│   │       parser_prescription.py
│   │       utils.py
│   │       db_utils.py
│   │
│   ├───mysql_scripts
│   │       queries.sql
│   │
│   ├───tests
│   │       test_prescription_parser.py
│   │
│   └───uploads                  # Temporary folder for PDF uploads
│
├───frontend
│       app.py                   # Streamlit UI
│
├───Notebooks
│       01_prescription_parser.ipynb
│       02_patient_details_parser.ipynb
│       03_RegEx.ipynb
│
└───reference
        tesseract_paper_by_google.pdf


