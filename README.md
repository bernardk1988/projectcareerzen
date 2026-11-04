# DocuMind – Multi-Format Processing Engine
![Python Logo](data/my.jpg)

## Overview

Documind is a Python-based  command-Line CLI  aplication designed to process multiple file formats such as 
- **PDF**
- **TXT**
- **XLSX**
- **JPG** 
Input file format.
It extracts text,tables,metadata,and important information from input files. it also uses Regular Expressions(Regex) to identify details such as email,address,phone numbers,dates, and invoice numbers.
- **CSV**
- **JSON**
output file format.
The extracted data can be displayed in the terminal and exported into CSV and JSON formats.

## Key Features

- *PDF Processing*: Extracts tables, metadata, and specific tables from PDF documents.

- *Excel Processing*: Reads XLSX files, handles missing values, and calculates summary statistics using Pandas.

- *Text Processing*: Extracts text using regular expression and raw text display save.

- *Image Processing*: Uses OCR to extract text from JPG images and metadata Identify.

- *Data Analysis*: Calculates row counts, sums, averages, and other relevant statistics for structured data.

- *Data Conversion*: Converts extracted and processed data into CSV or JSON formats.

- *Terminal Display*: Displays extracted data and processing summaries in a readable table format.

- *File Management*: Automatically locates input files and saves output files in the appropriate directories.

## Technology Stack
|Technology |Purpose|
|- Python|main programming language|
|- Argparse|-Command-line arguments|
|- pathlib|-file and folder handling|
|- Pandas|-excel and tabular data analysis|
|- PDFPlumber|-PDF text and table extraction|
|- Pillow|-image processing|
|- Pytesseract|-image OCR|
|- Regex(re)|-Extract important information|
|- Tabulate|-Display formated table|
|- Rich|-Terminal Display colourful|
|- JSON|-Store extrated data|
|- CSV|-Export extracted data|

## Project Structure
```
projectcareerzen/
src
├── documind.py
├── extractor/
│   ├── __init__.py
│   ├── extractor_pdf.py
│   ├── extractor_txt.py
│   ├── extractor_xlsx.py
│   └── extractor_jpg.py
├── converter/
│   ├── __init__.py
│   ├── converter_csv.py
│   └── converter_json.py
├── input/
│   └── parses.py
├── display/
│   └── display.py
│   └── display_table.py
├── CHANGE.log
├── SYSTEM.log
├── requirements.txt
└── README.md
```

## Workflow

- Accept input files and processing options through command-line arguments.

- Identify the file format and execute the appropriate extraction process.

- Clean and structure the extracted information.

- Calculate relevant statistics when applicable.

- Display the results in the terminal Tabulate/Rich.

- Export the processed data to CSV or JSON.

- Save the output files in the results directory.


## Installation

Install the required libraries:
- clone the repository
    git clone url(your github repository url)
- move into the project folder
    cd projectcareerzen
- bash
    pip install -r requirements.txt

## Usage

Run the following command from the project root:

- bash
    documind -f studentdetails.pdf --format pdf --output-format json --table 1

- bash
    documind -f studentdetails.pdf --format pdf --output-format csv --table 1

- bash
    documind -f studentdetails.pdf --format pdf --output-format json --table 2

- bash
    documind -f studentdetails.pdf --format pdf --output-format csv --table 1

- bash
    documind -f studentdetails.pdf --format pdf --output-format json --table 3

- bash
    documind -f studentdetails.pdf --format pdf --output-format csv --table 3

- bash
    documind -f student_invoice.txt --format txt --output-format json

- bash
    documind -f student_invoice.txt --format txt --output-format csv

same way image jpg and xlsx file format use

Replace `studentdetails.pdf` with your input filename. Place input files in the `data/` directory.

## Project Structure

The project separates input handling, extraction, conversion, and display logic into dedicated modules. 
This modular design makes the application easier to maintain, test, and extend with additional file formats and processing features.

## Purpose

DocuMind reduces manual document processing by providing a reusable command-line workflow for extracting, organizing, analyzing, and 
converting information from multiple file formats.