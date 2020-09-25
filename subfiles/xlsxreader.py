import pandas as pd


class Spreadsheet:
    def __init__(self, xlsx_path):
        self.xlsx_file = pd.read_excel(xlsx_path).values

    def get_xlsx_data(self):
        return self.xlsx_file
