
from pathlib import Path
import argparse

#pdf to csv and json
from extractor.extractor_pdf import extract_pdftable
from converter.converter_csv import save_csv_pdf
from converter.converter_json import save_json_pdf
from display.display_table import display_tables_onebyone,calculate_statistics_pdf
#calculate_statistics_pdf

# JPG extraction
from extractor.extractor_jpg import extract_table_jpg
from display.display import display_tables
#display_table1,
from converter.converter_csv import save_csv
from converter.converter_json import save_json

#xlsx
from extractor.extractor_xlsx import extract_data
from display.display_table import display_data
from converter.converter_csv import convert_to_csv1
from converter.converter_json import convert_to_json1

#text 
from extractor.extractor_text import extract_text,extract_invoice_details
from display.display import display_text
from converter.converter_csv import text_to_csv_save
from converter.converter_json import text_to_json_save

# parses.py is inside src/input/
BASE_DIR = Path(__file__).resolve().parents[2]
DATA_DIR = BASE_DIR / "data"
RESULTS_DIR = BASE_DIR / "results"


def parse():
    
    parser = argparse.ArgumentParser(
        description="DocuMind Multi-Format Processing Engine"
    )

    parser.add_argument(
        "-f", "--file",
        required=True,
        help="Input filename or file path"
    )

    parser.add_argument(
        "--format",
        choices=["pdf", "xlsx", "txt", "jpg"],
        required=True,
        help="Input file format"
    )

    parser.add_argument(
        "--absolute",
        action="store_true",
        help="Display the absolute input path"
    )

    parser.add_argument(
        "--output-format",
        choices=["csv", "json"],
        required=True,
        help="Output file format"
    )

    parser.add_argument(
        "--table",
        type=int,
        default=1,
        help="Table number, starting from 1"
    )

    args = parser.parse_args()

    if args.table < 1:
        parser.error("--table must be 1 or greater")

    # Resolve input path
    input_path = Path(args.file)

    if not input_path.is_absolute():
        if input_path.parent == Path("."):
            input_path = DATA_DIR / input_path
        else:
            input_path = BASE_DIR / input_path

    input_path = input_path.resolve()

    if not input_path.is_file():
        parser.error(f"Input file not found: {input_path}")

    # Create common results folder
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)

    if args.absolute:
        print("Absolute input path:", input_path)

    match args.format:

        case "pdf":
            print("Input format: PDF")
            try:
                df  = extract_pdftable(input_path,args.table)
                
                if df is None or df.empty:
                    raise ValueError("No table data found.")

                #Remove the title row, for example: Table 2 - Mark List
                df = df.iloc[1:].reset_index(drop=True)

                #Set the column headers from the first remaining row
                df.columns = (df.iloc[0].fillna("").astype(str).str.strip())

                #Remove the header row from the data
                df = df.iloc[1:].reset_index(drop=True)

                #Remove empty rows
                df = df.dropna(how="all").reset_index(drop=True)
               # Calculate statistics only for Table 2
                if args.table == 2:
                    df = calculate_statistics_pdf(df)
                display_tables_onebyone(df,args.table)

                #pages,metadata = extract_pdftable(input_path,args.table)
                #display_tables_onebyone(pages,metadata)

                output_path = (
                     RESULTS_DIR
                    / f"{input_path.stem}_table_{args.table}."
                       f"{args.output_format}"
                    )
                # output_path = (
                #                      RESULTS_DIR
                #                     / f"{input_path.stem}{args.table}.{args.output_format}"
                #                     )
                match args.output_format:
                    case "csv":
                        save_csv_pdf(df,output_path)
                    case "json":
                        save_json_pdf(df,output_path)
                        
                print("Saved:", output_path)
            except (ValueError, OSError) as error:
                parser.error(str(error))

    
        case "xlsx":
            print(f"Input format: {args.format.upper()}")

            try:
                df, row_count = extract_data(str(input_path))
                #print("Row count:", row_count)
                display_data(df,row_count)
                output_path = (
               RESULTS_DIR
                   / f"{input_path.stem}_table_{args.table}.{args.output_format}"
                )

                match args.output_format:
                    case "csv":
                        convert_to_csv1(df,row_count,output_path)
                    case "json":
                        convert_to_json1(df,row_count,output_path)

                print("Saved:", output_path)

            except (ValueError, OSError) as error:
                parser.error(str(error))
        case "txt":
            print("Input format: TXT")
            text = extract_text(input_path)
            df = extract_invoice_details(text)
            display_text(df,text)
            print("TXT processing is not implemented yet.")
            output_path = (
                           RESULTS_DIR
                               / f"{input_path.stem}_table_{args.table}.{args.output_format}"
                            )
            match args.output_format:
                case "csv":
                    text_to_csv_save(df,text,output_path)
                case "json":
                    text_to_json_save(df,text,output_path)

        case "jpg":
            print("Input format: JPG")

            try:
                text,metadata = extract_table_jpg(input_path)
                #df,metadata=display_table1(text,metadata)
                display_tables(text,metadata)
                output_path = (
                    RESULTS_DIR
                    / f"{input_path.stem}.{args.output_format}"
                )
                
                match args.output_format:
                    case "csv":
                        save_csv(text, metadata,output_path)
                    case "json":
                        save_json(text, metadata,output_path)
                
                print("Saved:", output_path)
            except (ValueError, OSError) as error:
                parser.error(str(error))
if __name__ == "__main__":
    parse()
