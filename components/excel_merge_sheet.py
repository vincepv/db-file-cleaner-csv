import pandas as pd

def merge_excel_sheet(excel_file):
    """
    inside the same excel file, merge all the sheets in one csv file
    merge based on column name 

    """

    df = pd.concat(pd.read_excel(excel_file, sheet_name=None), ignore_index=True)
    return df