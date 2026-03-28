# 📄 CamScanner using OpenCV

A document scanner web app built with Python, OpenCV and Streamlit.  
Upload any image and the app will automatically detect and highlight the document with green in it.

## 🌐 Live Demo
[Click here to try the app](https://camscanneripynb-7n8jj53mnhuxcspvmekxu6.streamlit.app/)

---

## 🖼️ How it Works
1. **Noise Removal** – Blurs the image to remove noise
2. **Edge Detection** – Detects edges in the blurred image
3. **Contour Extraction** – Extracts all contours from the image
4. **Best Contour** – Identifies the best 4-sided contour (the document)
5. **Output** – Displays the final result with document highlighted in green

---

## 🛠️ Libraries Used
- OpenCV (`cv2`)
- NumPy
- Streamlit
- Matplotlib
- Pillow

---

## 🚀 Run Locally

1. Clone the repo
```bash
   git clone https://github.com/yourusername/cam-scanner.git
   cd cam-scanner
```

2. Install dependencies
```bash
   pip install -r requirements.txt
```

3. Run the app
```bash
   streamlit run app.py
```

4. Open browser at `localhost:8501` and upload an image!

---

## 📂 Project Structure
```
cam-scanner/
├── scanner.ipynb        # Original Jupyter notebook
├── app.py               # Streamlit web app
├── requirements.txt     # Dependencies
└── sample_images/       # Test images
```

---

## 📸 Sample Output
<img width="1919" height="902" alt="image" src="https://github.com/user-attachments/assets/f2f35700-30a9-418d-a806-de925b6b8425" />
<img width="706" height="914" alt="image" src="https://github.com/user-attachments/assets/56bfbb0a-ca52-4bdb-b48e-31efd83ee47a" />



---

## 👤 Author
DIVYA SHARMA 
Gmail: divyasharma04aug@gmail.com
