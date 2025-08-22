import pandas as pd
import os

merge_pdf = pd.DataFrame()

for file in os.listdir(os.getcwd()):
    if file.endswith('.csv'):
        merge_pdf = merge_pdf._append(pd.read_csv(file))

merge_pdf.to_csv('mumbai.CSV', index=False)