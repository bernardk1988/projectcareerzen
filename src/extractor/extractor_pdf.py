import pdfplumber
import pandas as pd
from pathlib import Path


def extract_pdftable(input_file, table_number):
    with pdfplumber.open(input_file) as pdf:
        tables = []
        for page in pdf.pages:
            tables.extend(page.extract_tables())
    if not tables:
        raise ValueError("No tables found in PDF.")
    if table_number < 1 or table_number > len(tables):
        raise ValueError(
            f"Table {table_number} not found. "
            f"Available tables: {len(tables)}"
        )
    df = pd.DataFrame(tables[table_number - 1])
    return df

# def extract_pdftable(file_path):
#     pages=[]
#     with pdfplumber.open(file_path) as pdf:
#         for page_number,page in enumerate(pdf.pages,start=1):
#             text = page.extract_text() or ""
#             pages.append({"page_number":page_number,"text":text})
#             metadata = {
#                 "file_name":Path(file_path).name,
#                 "page_count":len(pdf.pages),
#                 "character_count":sum(len(page["text"]) for page in pages)
#             }
#         return pages,metadata

    