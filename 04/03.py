import pytesseract
from PIL import Image

#pytesseract.pytesseract.tesseract_cmd = r"D:\Chung_Hua_University\2024\Tesseract-OCR\tesseract.exe"
img = Image.open(r"word.jpg")
#img.show()
print(pytesseract.image_to_string(img, lang="chi_tra+eng"))
