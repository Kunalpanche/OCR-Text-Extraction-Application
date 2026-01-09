import streamlit as st
import pytesseract
from PIL import Image
import cv2
import numpy as np


pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)

# Streamlit Page Config
st.set_page_config(
    page_title="OCR Text Extractor",
    layout="centered"
)

st.title("📄 OCR Text Extractor")
st.write("Upload an image and extract text using OCR")

# File Upload
uploaded_file = st.file_uploader(
    "Upload an image",
    type=["png", "jpg", "jpeg"]
)

if uploaded_file is not None:
    # Load image
    image = Image.open(uploaded_file)

    # ✅ UPDATED: use width instead of use_column_width
    st.image(
        image,
        caption="Uploaded Image",
        width=500
    )

    # Convert PIL image → OpenCV format
    img = np.array(image)

    # Handle grayscale images safely
    if len(img.shape) == 3:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    else:
        gray = img

    # ===============================
    # OCR Button
    # ===============================
    if st.button("🔍 Extract Text"):
        with st.spinner("Extracting text..."):
            extracted_text = pytesseract.image_to_string(gray)

        st.subheader("📜 Extracted Text")
        st.text_area(
            "OCR Output",
            extracted_text,
            height=250
        )

        # Download extracted text
        st.download_button(
            label="⬇ Download Text",
            data=extracted_text,
            file_name="extracted_text.txt",
            mime="text/plain"
        )
