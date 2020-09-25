import pandas as pd


class Spreadsheet:
    def __init__(self, xlsx_path):
        """Initialising excel object which will read values through pandas library

        Args:
            xlsx_path (string): Path to xlsx file
        """
        self.xlsx_file = pd.read_excel(xlsx_path).values

    def get_xlsx_data(self):
        """Getting values from Excel spreadsheet

        Returns:
            [array]: Arrays of spreadsheet rows
        """
        return self.xlsx_file
