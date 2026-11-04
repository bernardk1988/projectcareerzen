from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)

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




