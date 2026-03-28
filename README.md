# 📄 CamScanner using OpenCV

A document scanner built with Python and OpenCV that detects and extracts documents from images.

## 🖼️ How it Works
1. **Noise Removal** – Blurs the image to remove noise
2. **Edge Detection** – Detects edges in the blurred image
3. **Contour Extraction** – Extracts all contours from the image
4. **Best Contour** – Identifies the best contour (the document)
5. **Output** – Displays the final scanned result

## 🛠️ Libraries Used
- OpenCV (`cv2`)
- NumPy
- Matplotlib

## 🚀 How to Run
1. Download or clone the repo
2. Install dependencies:
```bash
   pip install opencv-python numpy matplotlib
```
3. Open `scanner.ipynb` in Jupyter Notebook
4. Replace the image path with your own image
5. Run all cells

## 📂 Project Structure
```
cam-scanner/
├── scanner.ipynb       # Main notebook
└── sample_images/      # Test images
```
