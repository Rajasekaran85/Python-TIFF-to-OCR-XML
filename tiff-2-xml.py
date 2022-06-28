import sys
import os
import cv2
import pytesseract



'''
- Getting the Input file path from user
- language will be defined in "lang.ini" file in the same path of input files.
- language code should be three digit iso code, multiple language should be add by separation of "+" symbol. e.g.: eng+hin
- Tesseract version 5 should be installed in "C:\Program Files\Tesseract-OCR"
'''

print("\n OCR Tool - Output: Text format, ALTO format, hOCR format\n")
print("\n Developed by A Rajasekaran\n")
print("\n Date: 24 May 2022 \n\n")

filepath1 = input(" Enter the File path: ")

filepath = filepath1 + "\\"

filelist = os.path.isdir(filepath)


for fname in os.listdir(filepath):
    if not fname.endswith(".tif"):
        continue
    path = os.path.join(filepath, fname) 
    print(path)
    pytesseract.pytesseract.tesseract_cmd=r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    img = cv2.imread(path)  # load the image from the path using OpenCV library
    langu = filepath + "lang.ini"
    with open(langu) as f:   # open the ini file
        ini = f.read()       # read the ini file
    text = pytesseract.image_to_string(img, ini)    
    test = os.path.splitext(fname)[0]
    txtname = filepath + test + ".txt"
    f = open(txtname,"w+", encoding="utf-8")  
    f.write(text)

    alto = pytesseract.image_to_alto_xml(img)
    altoname = filepath + test + ".alto.xml"
    with open(altoname, 'w+b') as f:
        f.write(alto)

    hocr = pytesseract.image_to_pdf_or_hocr(img, extension='hocr')
    hocrname = filepath + test + ".hocr"
    with open(hocrname, 'w+b') as f:
        f.write(hocr)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

print("OCR Completed")
