from PIL import Image
import pytesseract

image = Image.open(r'C:/tmp/cnki.png')
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"
result = pytesseract.image_to_string(image)
print(result)
