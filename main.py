from pathlib import Path
from dotenv import load_dotenv
import os
from subfiles.xlsxreader import Spreadsheet
from subfiles.gmailsend import Gmailsend
from subfiles.emailtemplateextractor import Emailtemplate
from subfiles.bulksend import bulk_sending

PATH_XLSX = Path(Path.cwd(), "assets", "Database.xlsx")
PATH_ENV = Path(Path.cwd(), "envkeysfiles", ".env")
PATH_EMAIL_TITLE = Path(Path.cwd(), "assets",
                        "htmltemplates", "emailtitle.html")
PATH_EMAIL_BODY = Path(Path.cwd(), "assets",
                       "htmltemplates", "emailtemplate.html")

# Load data from .xlsx file
xlsx_file = Spreadsheet(PATH_XLSX)
xlsx_data = xlsx_file.get_xlsx_data()

# Loading enviornment variables
load_dotenv(dotenv_path=PATH_ENV)

# Sending emails
gmail_send = Gmailsend(os.getenv("GMAIL_EMAIL"))
email_template = Emailtemplate(
    PATH_EMAIL_TITLE, PATH_EMAIL_BODY)

bulk_sending(xlsx_data, gmail_send, email_template)
