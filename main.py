import os
import sys
import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
from pytesseract import Output

CONFIDENCE_THRESHOLD = 80.0
INPUT_FOLDER = "input_images"
OUTPUT_FOLDER = "output"


def preprocess_image(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    processed = cv2.adaptiveThreshold(
        blur, 255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        11, 2
    )
    return gray, blur, processed


def run_ocr(image, processed):
    config = "--psm 6"
    data = pytesseract.image_to_data(processed, config=config, output_type=Output.DICT)

    result_image = image.copy()
    lines = []
    confidences = []

    for i, text in enumerate(data["text"]):
        text = text.strip()
        try:
            confidence = float(data["conf"][i])
        except (ValueError, TypeError):
            confidence = -1

        if text and confidence >= CONFIDENCE_THRESHOLD:
            x = data["left"][i]
            y = data["top"][i]
            w = data["width"][i]
            h = data["height"][i]

            cv2.rectangle(result_image, (x, y), (x + w, y + h), (0, 180, 0), 2)
            cv2.putText(
                result_image,
                f"{text} ({confidence:.0f}%)",
                (x, max(20, y - 8)),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.55,
                (0, 120, 0),
                2,
                cv2.LINE_AA
            )

            lines.append(text)
            confidences.append(confidence)

    return result_image, lines, confidences


def main():
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)

    if len(sys.argv) > 1:
        image_path = sys.argv[1]
    else:
        files = [
            f for f in os.listdir(INPUT_FOLDER)
            if f.lower().endswith((".jpg", ".jpeg", ".png", ".bmp", ".webp"))
        ]
        if not files:
            print("No image found in input_images folder.")
            print("Put an image containing text in input_images and run the program again.")
            return
        image_path = os.path.join(INPUT_FOLDER, files[0])

    image = cv2.imread(image_path)
    if image is None:
        print(f"Could not read image: {image_path}")
        return

    gray, blur, processed = preprocess_image(image)
    result_image, lines, confidences = run_ocr(image, processed)

    cv2.imwrite(os.path.join(OUTPUT_FOLDER, "grayscale.png"), gray)
    cv2.imwrite(os.path.join(OUTPUT_FOLDER, "blurred.png"), blur)
    cv2.imwrite(os.path.join(OUTPUT_FOLDER, "processed.png"), processed)
    cv2.imwrite(os.path.join(OUTPUT_FOLDER, "ocr_result.png"), result_image)

    text = "\n".join(lines)
    with open(os.path.join(OUTPUT_FOLDER, "recognized_text.txt"), "w", encoding="utf-8") as file:
        file.write(text if text else "No text passed the 80% confidence threshold.\n")

    if confidences:
        average_confidence = sum(confidences) / len(confidences)
    else:
        average_confidence = 0

    with open(os.path.join(OUTPUT_FOLDER, "report.txt"), "w", encoding="utf-8") as file:
        file.write("AI Project 4 - OCR Report\n")
        file.write("=" * 30 + "\n")
        file.write(f"Input image: {os.path.basename(image_path)}\n")
        file.write(f"Confidence threshold: {CONFIDENCE_THRESHOLD:.0f}%\n")
        file.write(f"Accepted text items: {len(lines)}\n")
        file.write(f"Average confidence: {average_confidence:.2f}%\n\n")
        file.write("Recognized text:\n")
        file.write(text if text else "No text passed the confidence threshold.")

    print("\nOCR completed successfully.")
    print(f"Input: {image_path}")
    print(f"Accepted text items: {len(lines)}")
    print(f"Average confidence: {average_confidence:.2f}%")
    print("\nRecognized text:")
    print(text if text else "No text passed the 80% confidence threshold.")
    print(f"\nResults saved in: {OUTPUT_FOLDER}")


if __name__ == "__main__":
    main()
