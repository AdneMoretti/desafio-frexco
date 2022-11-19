from datetime import date
import csv
import pandas as pd
import numpy as np
import json


class Utils():
    def format_date(self, dataNascimento):
        day, month, year = dataNascimento.split('/')
        data = date(int(year), int(month), int(day))
        return data


    def write_csv(data):
        if(len(data)>0):
            keys = data[0].keys()
            with open('data.csv', 'w', newline='') as output:
                csv_writer = csv.DictWriter(output, keys)
                csv_writer.writeheader()
                csv_writer.writerows(data)
            

    def write_xsls(data):
        data_csv = pd.read_csv('data.csv') 
        excel_writer = pd.ExcelWriter('data.xlsx') 
        data_csv.to_excel(excel_writer, index = False) 
        excel_writer.save() 

    
    def write_json(data):
        with open("data.json", "w") as outfile: 
            json.dump(data, outfile , indent=4)

