from datetime import datetime
import csv
import pandas as pd
import numpy as np
import openpyxl

class Utils():
    def format_date(self, dataNascimento):
        dia, mes, ano = dataNascimento.split('/')
        data = datetime(int(ano), int(mes), int(dia))
        return data

    def write_csv(data):
        keys = data[0].keys()

        with open('data.csv', 'w', newline='') as output:
            dict_writer = csv.DictWriter(output, keys)
            dict_writer.writeheader()
            print(dict_writer.writerows(data))
            

    def write_xsls(data):
        df_new = pd.read_csv('data.csv') 
        print(df_new)
        GFG = pd.ExcelWriter('data.xlsx') 
        data.to_excel(GFG, index = False) 
        
        GFG.save() 


