import sqlite3

import pandas as pd

# ADD FILE TO THE SAME FOLDER AND REPLACE FILENAME
filename="example"

con=sqlite3.connect(filename+".db")
wb=pd.ExcelFile(filename+'.xlsx')
for sheet in wb.sheet_names:
        df=pd.read_excel(filename+'.xlsx',sheet_name=sheet)
        df.to_sql(sheet,con, index=False,if_exists="replace")
con.commit()
con.close()
