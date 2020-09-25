from pathlib import Path
from subfiles.xlsxreader import Spreadsheet
from subfiles.gmailsend import Gmailsend

PATH_XLSX = Path(Path.cwd(), "assets", "Database.xlsx")

xlsx_file = Spreadsheet(PATH_XLSX)
xlsx_data = xlsx_file.get_xlsx_data()
print(xlsx_data)
