import os
from PIL import Image
import pyocr

#インストールしたTesseract-OCRのパスを環境変数「PATH」へ追記する。
#OS自体に設定してあれば以下の2行は不要
path='C:\\Program Files\\Tesseract-OCR'
os.environ['PATH'] = os.environ['PATH'] + path

#pyocrへ利用するOCRエンジンをTesseractに指定する。
tools = pyocr.get_available_tools()
tool = tools[0]

with open("fullmp4.txt", "w") as outputfile:
    for i in range(10000):
        filename=str(i)+"_t.jpg"

        if not os.path.isfile(filename):
            break
        img = Image.open(filename)

        builder = pyocr.builders.TextBuilder(tesseract_layout=6)
        text = tool.image_to_string(img, lang="jpn", builder=builder)
        num = text.splitlines()

        print(" ".join(num), file=outputfile)
        # outputfile.write(" ".join(num))
        # outputfile.write("\r")
        print(i)

        os.remove(filename)