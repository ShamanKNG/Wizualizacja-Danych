import pandas as pd
import numpy as np
import xlrd
import openpyxl

imiona = pd.ExcelFile('G:\PatrykS\Wizualizacjadanych\srodowisko\Lista 8\imiona.xlsx')
df = pd.read_excel(imiona,'Arkusz1')
print(df)
