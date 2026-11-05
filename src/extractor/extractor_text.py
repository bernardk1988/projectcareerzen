from pathlib import Path
import re
import pandas as pd

def extract_text(input_file):
    input_file=Path(input_file)
    with open(input_file,"r",encoding="utf-8") as file:
        text = file.read()
        return text

def extract_invoice_details(text):
    patterns = {
    "Invoice Number": r"Invoice Number:\s*(.+)","Date":r"Date:\s*(\d{2}-\d{2}-\d{4})","Email":r"[\w.+-]+@[\w.-]+\.\w+","Total":r"Total:\s*Rs\.?\s*([\d,]+)"
    }
    data={}
    for key,pattern in patterns.items():
        match = re.search(pattern,text,re.IGNORECASE)
        if match:
            if key == "Email":
                data[key]=match.group(0)
            else:
                data[key]=match.group(1).strip()
        else:
            data[key]= ""
    return pd.DataFrame([data])




