import pandas as pd

def leer_db_excel():
    archivo = pd.read_excel('matriculas.xlsm', sheet_name='BD')