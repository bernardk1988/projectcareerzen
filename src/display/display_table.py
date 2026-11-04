
#pdf 
# from tabulate import tabulate

# def display_tables_onebyone(pages,metadata):
#     print("\nPDF Metadata")
#     print(tabulate([{"Field":key,"Values":value} for key,value in metadata.items()],
#                    headers="keys",tablefmt="grid"))
#     print("\nExtracted PDF Text")
#     for page in pages:
#         print(f"\n---Page{page['page_number']}----")
#         print(page["text"] or "No selectable text found")


from tabulate import tabulate
import pandas as pd
print("\nSTUDENT MARK DETAILS")
def display_tables_onebyone(df, table_number):
    print(f"\nExtracted Table {table_number}")
    print(f"Table {table_number} Row count:{len(df)}")
    print(tabulate(df,headers="keys",tablefmt="rounded_grid",showindex=False))

def calculate_statistics_pdf(df):
    mark_columns = ["Tamil", "English", "Maths"]

    # Check subject columns
    if not all(col in df.columns for col in mark_columns):
        print("No mark columns found:", list(df.columns))
        return df

    for col in mark_columns:
        df[col] = pd.to_numeric(df[col], errors="coerce")

  
    df["Sum"] = df[mark_columns].sum(axis=1)
    df["Average"] = df[mark_columns].mean(axis=1).round(2)

    highest_mark = df[mark_columns].max().max()


    highest_row = df[mark_columns].max(axis=1).idxmax()

    stdId=df.loc[highest_row, "Student ID"]
    highest_sum = df["Sum"].max()

    highest_average = df["Average"].max()


    #Display summary
    summary = [
        ["Row Count:",len(df)],
        ["Student Id:",stdId],
        ["Max Mark:",highest_mark],
        ["Heightest Avg:",highest_average],
        ["Highest Sum:",highest_sum],
    ]
    print("\nMARK SUMMARY")
    print(tabulate(
        summary,
        headers=["Description","Value"],
        tablefmt="fancy_grid"
    ))
    return df


#xlsx 

from tabulate import tabulate

def display_data(df,row_count):
    print(tabulate(
        df,headers="keys",tablefmt="rounded_grid",showindex=False,
    ))
    print(tabulate(
           [["Row Count",row_count]],headers=["Description","value"],tablefmt="rounded_grid"
       ))
    #print("Row count:",len(df)-1)
