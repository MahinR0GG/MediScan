import streamlit as st
import requests
from pdf2image import convert_from_bytes
import json
import time
import os

# ----------------------------
# Set Poppler path for Windows
# ----------------------------
POPPLER_PATH = r"C:/poppler-25.07.0/Library/bin"
os.environ["PATH"] += os.pathsep + POPPLER_PATH

# ----------------------------
# Backend URL
# ----------------------------
URL = "http://127.0.0.1:8000/{}"

st.title("MediScan - Medical Data Extractor 👩‍⚕️")

# ----------------------------
# File uploader and options
# ----------------------------
file = st.file_uploader("Upload PDF", type="pdf")
col1, col2 = st.columns(2)

with col1:
    file_format = st.radio(
        label="Select type of document",
        options=["prescription", "patient_details"],
        horizontal=True
    )

with col2:
    if file and st.button("Upload PDF"):
        bar = st.progress(50)
        time.sleep(1)
        bar.progress(100)
        payload = {'file_format': file_format}
        files = [('file', file.getvalue())]
        try:
            response = requests.post(URL.format('extract_from_doc'), data=payload, files=files)
            dict_str = response.content.decode("UTF-8")
            data = json.loads(dict_str)  # safer than ast.literal_eval
            st.session_state['data'] = data
        except Exception as e:
            st.error(f"Error contacting backend: {e}")

# ----------------------------
# Display PDF and extracted data
# ----------------------------
if file:
    try:
        pages = convert_from_bytes(file.getvalue(), poppler_path=POPPLER_PATH)
        st.subheader("Your PDF")
        st.image(pages[0])  # display first page

    except Exception as e:
        st.error(f"PDF rendering failed: {e}")

    # Show extracted details
    if 'data' in st.session_state:
        st.subheader("Extracted Details")
        extracted = st.session_state['data']

        if file_format == "prescription":
            name = st.text_input("Name", value=extracted.get("patient_name", ""))
            address = st.text_input("Address", value=extracted.get("patient_address", ""))
            medicines = st.text_input("Medicines", value=extracted.get("medicines", ""))
            directions = st.text_input("Directions", value=extracted.get("directions", ""))
            refill = st.text_input("Refill", value=extracted.get("refill", ""))
        else:  # patient_details
            name = st.text_input("Name", value=extracted.get("patient_name", ""))
            phone = st.text_input("Phone No.", value=extracted.get("phone_no", ""))
            vacc_status = st.text_input("Hepatitis B vaccination status", value=extracted.get("vaccination_status", ""))
            med_problems = st.text_input("Medical Problems", value=extracted.get("medical_problems", ""))
            has_insurance = st.text_input("Has insurance?", value=extracted.get("has_insurance", ""))

        # ----------------------------
        # Submit button
        # ----------------------------
        if st.button("Submit"):
            try:
                if file_format == "prescription":
                    payload = {
                        "name": name,
                        "address": address,
                        "medicines": medicines,
                        "directions": directions,
                        "refill": refill
                    }
                else:
                    payload = {
                        "name": name,
                        "phone": phone,
                        "vacc_status": vacc_status,
                        "med_problems": med_problems,
                        "has_insurance": has_insurance
                    }

                resp = requests.post(URL.format(file_format), data=payload)
                result = json.loads(resp.content.decode("UTF-8"))
                if result:
                    st.success("Details successfully recorded.")
                    st.session_state.pop('data', None)
                else:
                    st.error("Error saving data to database.")
            except Exception as e:
                st.error(f"Error sending data: {e}")

#streamlit run app.py