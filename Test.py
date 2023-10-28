import pandas as pd


inputFile= pd.read_excel(r"InputFile.xlsx", sheet_name='Sheet1')


inputFile.to_excel('output/output/outputFile.xlsx', index=False)