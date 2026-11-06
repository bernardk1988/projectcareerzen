from PIL import Image
# import pytesseract
# import os
import os
import shutil
import pytesseract

# if os.name == "nt":
#    pytesseract.pytesseract.tesseract_cmd = (r"C:\Program Files\Tesseract-OCR\tesseract.exe")
# else:
#    pytesseract.pytesseract.tesseract_cmd = "/usr/bin/tesseract"
if os.name == "nt":

    # Windows
    pytesseract.pytesseract.tesseract_cmd = (
        r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    )

else:

    # Linux - PythonAnywhere
    tesseract_path = shutil.which("tesseract")

    if not tesseract_path:
        raise FileNotFoundError("Tesseract OCR is not installed")

    pytesseract.pytesseract.tesseract_cmd = tesseract_path

def extract_table_jpg(input_file):
    image = Image.open(input_file)
    metadata ={
        "File Name":input_file.name,
        "Image format":image.format,
        "Width":image.width,
        "height":image.height,
        "Color Mode":image.mode,
    }
    image = image.convert("L")
    text = pytesseract.image_to_string(image)
    return text,metadata




