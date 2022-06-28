# Project Title

TIFF to OCR XML Application

## Description

* pytesseract, pillow library used
* OCR the TIFF Images
* Output format: Text format, ALTO format, hOCR format
* language will be defined in "lang.ini" file in the same path of input files.
* language code should be three digit iso code
* Multiple language should be add by separation of "+" symbol. e.g.: eng+dan

## Getting Started

### Dependencies

* Windows 7

### Installing

* pip install pytesseract
* Tesseract version 5 should be installed in "C:\Program Files\Tesseract-OCR"

### Executing program

* "lang.ini" file should copied in the tool path
* Run the program
* Tool will ask to enter the path of the input TIF file
* Tool execute the TIFF file and create the output file in 3 formats: Text format, ALTO format, hOCR format in the same input file path

### Help

* language will be defined in "lang.ini" file in the same path of input files.
* language code should be three digit iso code
* Multiple language should be add by separation of "+" symbol. e.g.: eng+dan



## Version History

* 0.1
    * Initial Release
