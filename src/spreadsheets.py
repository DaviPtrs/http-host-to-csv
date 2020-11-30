import os
import pandas as pd
import glob

def join_csvs(path):
    all_files = glob.glob(os.path.join(path, "*.csv"))
    print("Joining CSVs")

    writer = pd.ExcelWriter('out.xlsx', engine='xlsxwriter')
    
    for f in all_files:
        df = pd.read_csv(f)
        df.to_excel(writer, sheet_name=os.path.splitext(os.path.basename(f))[0], index=False)

    writer.save()

    print(f"Output spreadsheet located on {path}/out.xlsx")
