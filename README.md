# Artificial Intelligence Project 4: OCR Text Recognition

## Project Overview

This project is a basic Image Text Recognition system developed using Python, OpenCV and Tesseract OCR.

The system takes an image containing text as input, processes the image using different image preprocessing techniques, and extracts the text from the image using Optical Character Recognition (OCR).

The project also calculates confidence scores for the recognized text and saves the extracted text and processed images in the output folder.

## Objective

The main objective of this project is to understand how OCR can be used to extract text from images.

The project demonstrates:

* Image loading
* Image preprocessing
* Grayscale conversion
* Gaussian Blur
* Adaptive Thresholding
* Text extraction using Tesseract OCR
* Confidence score checking
* Saving recognized text
* Saving processed images

## Key Features

* Reads text from an image
* Converts the image into grayscale
* Applies Gaussian Blur to reduce noise
* Uses Adaptive Thresholding for better text recognition
* Extracts text using Tesseract OCR
* Uses an 80% confidence threshold
* Saves the recognized text into a text file
* Saves processed images for reference
* Generates a project report

## Technologies Used

* Python
* OpenCV
* Pytesseract
* Tesseract OCR
* NumPy

## Image Preprocessing

The project uses the following preprocessing steps:

### Grayscale

The input image is converted into grayscale to simplify the image and make text recognition easier.

### Gaussian Blur

Gaussian Blur is applied to reduce noise from the image.

### Adaptive Thresholding

Adaptive Thresholding converts the image into a suitable black-and-white format so that the text can be detected more clearly.

## OCR

OCR stands for Optical Character Recognition.

Tesseract OCR is used in this project to recognize and extract text from the processed image.

The project uses a confidence threshold of 80% to filter recognized text.

## Project Flow

```text
Input Image
     ↓
Read Image
     ↓
Grayscale Conversion
     ↓
Gaussian Blur
     ↓
Adaptive Thresholding
     ↓
Tesseract OCR
     ↓
Confidence Checking
     ↓
Extracted Text
     ↓
Save Results
```

## Folder Structure

```text
AI_Project_4_OCR/
│
├── main.py
├── README.md
├── requirements.txt
├── run_project.bat
│
├── input_images/
│   └── sample_text.png
│
└── output/
    ├── grayscale.png
    ├── blurred.png
    ├── processed.png
    ├── ocr_result.png
    ├── recognized_text.txt
    └── report.txt
```

## Installation

First install the required Python libraries:

```bash
pip install opencv-python pytesseract numpy
```

Tesseract OCR software must also be installed on the computer.

After installing Tesseract, make sure its installation path is correctly configured in the Python program.

## How to Run

1. Place the input image inside the `input_images` folder.
2. Open the project folder in VS Code.
3. Open the terminal.
4. Run the following command:

```bash
python main.py
```

5. The program will process the image and perform OCR.
6. The recognized text and processed images will be saved in the `output` folder.

## Sample Input

The project includes a sample image:

```text
input_images/sample_text.png
```

The sample image contains text related to this Artificial Intelligence project.

## Output

After running the project, the following files are generated:

* `grayscale.png` – grayscale version of the input image
* `blurred.png` – blurred image
* `processed.png` – processed image used for OCR
* `ocr_result.png` – image containing OCR results
* `recognized_text.txt` – extracted text
* `report.txt` – project processing report

## Confidence Threshold

The project uses an **80% confidence threshold**.

Only text recognized with sufficient confidence is considered for the final result.

## Example

Input:

```text
ARTIFICIAL INTELLIGENCE PROJECT 4
Basic Image Text Recognition using OCR
Student Name: Nidhish Bhardwaj
Technology: Python, OpenCV and Tesseract OCR
Confidence Threshold: 80%
```

The OCR system processes the image and extracts the text into a text file.

## Applications

OCR technology can be used in:

* Document digitization
* Reading printed documents
* Extracting text from images
* Invoice processing
* Form processing
* Automated document management
* Text recognition systems

## Limitations

The accuracy of OCR depends on image quality, font style, lighting, noise and text clarity.

Handwritten text and very low-quality images may not be recognized accurately.

## Project Information

**Project:** Artificial Intelligence Project 4
**Title:** Basic Image Text Recognition using OCR
**Student:** Nidhish Bhardwaj
**Technology:** Python, OpenCV and Tesseract OCR
**Confidence Threshold:** 80%

## Conclusion

This project demonstrate
