import pandas as pd
from openpyxl import load_workbook


class Spreadsheet:
    def __init__(self, xlsx_path):
        """Initialising excel object which will read values through pandas library

        Args:
            xlsx_path (string): Path to xlsx file
        """
        self.path = xlsx_path
        self.xlsx_file_pd = pd.read_excel(self.path)
        self.xlsx_file_op = load_workbook(self.path)

    def get_xlsx_data(self):
        """Getting values from Excel spreadsheet

        Returns:
            [array]: Arrays of spreadsheet rows
        """
        return self.xlsx_file_pd

    def add_to_row(self, row_number, text):
        workbook = self.xlsx_file_op.active
        workbook.cell(column=workbook.max_column,
                      row=row_number+1, value=text)
        self.xlsx_file_op.save(self.path)
