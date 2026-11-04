import csv
from pathlib import Path
import pandas as pd

#image
def save_csv(text,metadata,output_path):
    # metadata_df = pd.DataFrame(list(metadata.items()),columns=["Property","Value"])
    # with open(output_path,"w",encoding="utf-8",newline="\n") as file:
    #     metadata_df.to_csv(file,index=False)
    #     file.write("\n") 
    #     df.to_csv(file,index=False)
    # return output_path
    data = {
        "Raw_text":text,
        **metadata
    }
    df=pd.DataFrame([data])
    df.to_csv(output_path,index=False)

#xlsx
def convert_to_csv1(df,row_count,output_path):
    df.to_csv(output_path,index=False,encoding="utf-8")
    with open(output_path,"a",encoding="utf-8") as file:
        file.write(f"\nRow count:{row_count}\n")

#text 

def text_to_csv_save(df,text,output_path):
    df.to_csv(output_path,index=False,encoding="utf-8")
    with open(output_path,"a",encoding="utf-8",newline="\n") as file:
        pd.DataFrame({"Raw_text":[text]}).to_csv(file,index=False)

#pdf 

def save_csv_pdf(df, output_path):
    # Create the results folder if it does not exist
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    # Convert table to CSV
    df.to_csv(output_path, index=False, encoding="utf-8")

    print(f"CSV saved: {output_path}")

# def save_csv_pdf(pages,metadata,output_path):
#     rows=[]

#     for key,value in metadata.items():
#         rows.append({"type":"metadata","page_number":"","field":key,"text":str(value)})
#     for page in pages:
#         rows.append({"type":"page_text","page_number":page["page_number"],"field":"text","text":page["text"]})
#         output_path =Path(output_path)
#         output_path.parent.mkdir(parents=True,exist_ok=True)
#         df=pd.DataFrame(rows)
#         df.to_csv(output_path,index=False,encoding="utf-8-sig")
#         return output_path
