# Task-4-nidhish_bhardwaj

## Image or Text Recognition (Basic) - OCR Path

### Project objective
Build a basic image-recognition pipeline that takes an image, prepares it using image processing, and extracts readable text using a pre-trained OCR engine.

This implementation follows the **OCR path** described in the Project 4 PDF.

### Technologies used
- Python
- OpenCV (`cv2`)
- Pytesseract
- Tesseract OCR

### Processing pipeline
```text
Input Image
    |
    v
Read image with OpenCV
    |
    v
Grayscale conversion
    |
    v
Gaussian blur
    |
    v
Adaptive thresholding
    |
    v
Tesseract OCR (PSM 6)
    |
    v
Confidence filtering (>= 80%)
    |
    v
Recognized text + bounding boxes
```

### PDF requirements covered
1. Use a pre-trained recognition library: Pytesseract/Tesseract.
2. Use OpenCV for image processing.
3. Convert the image to grayscale.
4. Apply Gaussian blur to reduce small noise.
5. Apply adaptive thresholding to create a binary image.
6. Use OCR with page segmentation mode (`--psm 6`).
7. Keep detections with confidence of at least 80%.
8. Produce a clear visual output with bounding boxes and confidence values.

### Project structure
```text
AI_Project_4_OCR/
|
|-- main.py
|-- requirements.txt
|-- README.md
|-- run_project.bat
|
|-- input_images/
|   |-- sample_text.png
|
`-- output/
    |-- grayscale.png
    |-- blurred.png
    |-- processed.png
    |-- ocr_result.png
    |-- recognized_text.txt
    `-- report.txt
```

### Installation

#### 1. Install Python packages
Open Command Prompt in the project folder and run:

```bash
pip install -r requirements.txt
```

#### 2. Install Tesseract OCR
Install the Tesseract OCR engine on Windows. If Tesseract is not in PATH, add its executable location to PATH or set `pytesseract.pytesseract.tesseract_cmd` in `main.py`.

### Run the project
The easiest method on Windows is:

```text
run_project.bat
```

Or run directly:

```bash
python main.py
```

The program automatically uses the first image inside `input_images`.

You can also provide a specific image:

```bash
python main.py input_images\sample_text.png
```

### Output
The program creates:

- `grayscale.png` - grayscale image
- `blurred.png` - Gaussian-blurred image
- `processed.png` - adaptively thresholded image
- `ocr_result.png` - original image with accepted OCR boxes and confidence values
- `recognized_text.txt` - extracted text
- `report.txt` - small project result report

### Important note
The PDF presents two possible implementation paths: **OCR** and **Object Detection with MobileNet-SSD**. This project implements the OCR path. The PDF's object-detection path is therefore not included in this version.
