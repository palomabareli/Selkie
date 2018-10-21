#/usr/bin/python3
# -*- coding: UTF-8 -*-

import pandas as pd
import csv
import json

folder = '/home/paloma/Documents/Estudos/DataBase/BaseDerivad/'
fileOrigin = 'serienova.csv' #'serie_tempo_gelo_do_mar.csv'
fileDestination = 'serienova.csv' #'serie_tempo_gelo_do_mar_short.json'

folderFileOrigin = folder + fileOrigin
folderFileDestination = folder + fileDestination

data = pd.DataFrame()

def leituraCSV():
    try:
        data = pd.read_csv(folderFileOrigin)
        print(data.head(5))
    except Exception as ex:
        print(ex.message)

def writeFileJSON():
    try:
        csv_file = pd.DataFrame(pd.read_csv(folderFileOrigin, sep = ";", header = 0, index_col = False))
        csv_file.to_json(folderFileDestination, orient = "records", date_format = "epoch", double_precision = 10, force_ascii = True, date_unit = "ms", default_handler = None)
    except Exception as ex:
        print(ex.message)      

#leituraCSV()
writeFileJSON()

