import easyocr


reader = easyocr.Reader(['ch_tra','en'])
text = reader.readtext("word.jpg")

for item in text:
    print(item[1])