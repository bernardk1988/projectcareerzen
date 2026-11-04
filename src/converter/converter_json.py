
from pathlib import Path
import json

#image
def save_json(text, metadata,output_path):
    # Convert DataFrame into JSON records
    # data={
    #     "metadata":metadata,
    #     "word_count":len(df),
    #     "extracted_data":df.to_dict(orient="records")
    # }
    # with open(output_path,"w",encoding="utf-8") as file:
    #     json.dump(data,file,indent=4,ensure_ascii=False)
    # return output_path
    data = {
        "raw_text":text,
        "metadata":metadata,
    }
    with open(output_path,"w",encoding="utf-8") as file:
        json.dump(data,file,indent=4,ensure_ascii=False,default=str)
    print(f"Json Saved:{output_path}")
#xlxs

def convert_to_json1(df,row_count,output_path):
    data ={
        "Row count":row_count,
        "data":df.to_dict(orient="records")
    }
    with open(output_path,"w",encoding="utf-8") as file:
        json.dump(
            data,file,indent=4,ensure_ascii=False
        )

#text

def text_to_json_save(df, text,output_path):
    data={"data":df.to_dict(orient="records"),"Raw_text":text}
    with open(output_path,"w",encoding="utf-8") as file:
        json.dump(data,file,indent=4,ensure_ascii=False)
    print(f"JSON Saved Successfully{output_path}")

#pdf 
def save_json_pdf(df, output_path):
# def save_json_pdf(pages,metadata,output_path):
#     # Create the results folder if it does not exist
#     result={
#         "metadata":metadata,
#         "pages":pages
#     }
#     output_path = Path(output_path)
#     output_path.parent.mkdir(parents=True, exist_ok=True)
#     with open(output_path,"w",encoding="utf-8") as file:
#         json.dump(result,file,indent=4,ensure_ascii=False)
#     return output_path


    # Convert table to JSON
    df.to_json(
        output_path,
        orient="records",
        indent=4,
        force_ascii=False
    )

    print(f"JSON saved: {output_path}")
