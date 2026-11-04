
import pandas as pd


def extract_data(input_file):
    df = pd.read_excel(input_file)
    df =df.fillna(0)
    columns = ["Tamil","English","Maths"]
    for column in columns:
        df[column]=pd.to_numeric(df[column],errors="coerce").fillna(0)
    df["Sum"]=df[columns].sum(axis=1)
    df["Average"]=df[columns].mean(axis=1).round(2)
    total_row={
        "Name":"Total",
        "Tamil":df["Tamil"].sum(),
        "English":df["English"].sum(),
        "Maths":df["Maths"].sum(),
        "Sum":df["Sum"].sum(),
        "Average":round(df["Average"].mean(),2),
    }
    df.loc[len(df)] = total_row
    row_count = len(df)-1
    return df,row_count



