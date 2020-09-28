from pathlib import Path
from dotenv import load_dotenv
import os
from subfiles.xlsxreader import Spreadsheet
from subfiles.gmailsend import Gmailsend
from subfiles.emailtemplateextractor import Emailtemplate
from subfiles.emailfinder import Emailfinder
from subfiles.bulksend import bulk_sending

PATH_ENV = Path(Path.cwd(), "envkeysfiles", ".env")
# Loading enviornment variables
load_dotenv(dotenv_path=PATH_ENV)

PATH_XLSX = Path(Path.cwd(), "assets", "Database.xlsx")
PATH_EMAIL_TITLE = Path(Path.cwd(), "assets",
                        "htmltemplates", "emailtitle.html")
PATH_EMAIL_BODY = Path(Path.cwd(), "assets",
                       "htmltemplates", "emailtemplate.html")
PATH_EMAIL_ATTACHMENT = Path(Path.cwd(), "assets",
                             "attachments", os.getenv("ATTACHMENT_NAME"))

# Loading data from .xlsx file
xlsx_file = Spreadsheet(PATH_XLSX)

# Loading template from HTML file
email_template = Emailtemplate(
    PATH_EMAIL_TITLE, PATH_EMAIL_BODY)

# Loading email address finding details
email_finder = Emailfinder(str(os.getenv("HUNTER_API_KEY")))

# Sending emails
gmail_send = Gmailsend(os.getenv("GMAIL_EMAIL"), os.getenv("GMAIL_ALIAS"))

bulk_sending(xlsx_file, gmail_send, email_template,
             str(PATH_EMAIL_ATTACHMENT), email_finder)
