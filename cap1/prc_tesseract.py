# https://qiita.com/yoshi_yast/items/bd5e1e91ac9f64157203

import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
url_img = '345_trimmed.jpg'
img = Image.open(url_img)
number = pytesseract.image_to_string(img)
print (number)


