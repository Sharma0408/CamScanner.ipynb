import cv2
import numpy as np
import streamlit as st
from PIL import Image

st.title("📄 CamScanner using OpenCV")
st.write("Upload an image to get a clean scanned output")

uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:

    # Read image
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

    st.subheader("Original Image")
    st.image(img, channels="BGR")

    # Step 1 - Remove noise / blur
    blurred = cv2.GaussianBlur(img, (5, 5), 0)

    # Step 2 - Edge detection
    edges = cv2.Canny(blurred, 75, 200)

    st.subheader("Edge Detection")
    st.image(edges)

    # Step 3 - Contour extraction
    contours, _ = cv2.findContours(edges, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)

    # Step 4 - Best contour
    best_contour = None
    for c in contours:
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.02 * peri, True)
        if len(approx) == 4:
            best_contour = approx
            break

    # Step 5 - Show result
    if best_contour is not None:
        output = img.copy()
        cv2.drawContours(output, [best_contour], -1, (0, 500, 0), 3)
        st.subheader("Document Detected ✅")
        st.image(output, channels="BGR")
    else:
        st.warning("No document contour found. Try a clearer image.")