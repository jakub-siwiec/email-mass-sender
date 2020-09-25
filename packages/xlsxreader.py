import pandas as pd
from pathlib import Path


class Spreadsheet:
    def __init__(self):
        self.xlsx_path = Path(Path.cwd()).parent.joinpath(
            'assets', 'Database.xlsx')
        self.xlsx_file = pd.read_excel(self.xlsx_path).values
        print(self.xlsx_path)
        print(self.xlsx_file)


hi = Spreadsheet()
