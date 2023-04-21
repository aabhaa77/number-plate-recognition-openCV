from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = (
    r'C:\\Users\\aabha\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract'
)

img = r"ocr-test.png"

print(pytesseract.image_to_string(Image.open(img)))