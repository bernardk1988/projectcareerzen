import pandas as pd
from tabulate import tabulate
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
console = Console()

#text
def display_text(df,text):
    table = Table(
                  title ="📝Extracted Invoice Details",
                  title_style= "bold cyan",
                  border_style="bright_blue",
                  header_style ="bold white on dark_blue",
                  show_lines=True,
                  )
    table.add_column("Field",style="bold yellow")
    table.add_column("Extracted Value",style="bright_green")
    for column in df.columns:
        value = str(df.iloc[0][column])
        table.add_row(column,value)
    summary = Text()
    summary.append("Total Records:",style="bold white")
    summary.append(str(len(df)),style="bold bright_yellow")
    console.print(
        Panel(
            table,
            title="[bold magenta]DocuMind[/bold magenta]",
            subtitle="[italic cyan]Data Transafermation & Structuring[/italic cyan]",
            border_style="bright_magenta",padding=(1,2),
            style="white on dark_blue"
        )
    )
    console.print(
        Panel(summary,title="[bold green]Summery[/bold green]",border_style="green",expand=False)
    )
    
    console.print(Panel(
        text,
        title="[bold magenta]Raw Text[/bold magenta]",
        subtitle="[italic cyan]END[/italic cyan]",
        border_style="red",expand=False,
        padding=(1,4),
        style="white on black"
    ))

    #console.print(table)

#image
# def display_table1(text,metadta):
#     data = {
#         "Line No": [],
#         "Extracted Text": []
#     }
#     for number,line in enumerate(text.splitlines(),start=1):
#         if line.strip():
#             data["Line No"].append(number)
#             data["Extracted Text"].append(line.strip())
#     df=pd.DataFrame(data)
#     return df,metadta
        
def display_tables(text,metadata):
    print("\nImage Metadata")
    print(tabulate(list(metadata.items()),
                   headers=["property","Value"],
                   tablefmt="grid"
                   ))
    print("\nExtracted OCR Text")
    print(text)
    print("word Count:",len(text))

