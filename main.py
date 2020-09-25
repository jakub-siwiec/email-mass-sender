from pathlib import Path
from dotenv import load_dotenv
import os
from subfiles.xlsxreader import Spreadsheet
from subfiles.gmailsend import Gmailsend

PATH_XLSX = Path(Path.cwd(), "assets", "Database.xlsx")
PATH_ENV = Path(Path.cwd(), "envkeysfiles", ".env")

# Load data from .xlsx file
xlsx_file = Spreadsheet(PATH_XLSX)
xlsx_data = xlsx_file.get_xlsx_data()
print(xlsx_data)

# Loading enviornment variables
load_dotenv(dotenv_path=PATH_ENV)

# Sending emails
gmail_send = Gmailsend(os.getenv("GMAIL_EMAIL"),
                       os.getenv("GMAIL_EXPERIMENT_SENDER"), "Test", "Test content")
gmail_send.send()
