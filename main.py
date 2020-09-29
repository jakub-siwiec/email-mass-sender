from pathlib import Path
from dotenv import load_dotenv
import os
from subfiles.xlsxreader import Spreadsheet
from subfiles.gmailsend import Gmailsend
from subfiles.emailtemplateextractor import Emailtemplate
from subfiles.templatescontainer import Templatescontainer
from subfiles.emailfinder import Emailfinder
from subfiles.bulksend import Bulksending


def main():
    # Confirmation for sending emails
    input_value = input(
        "\nPlease double check the correctness of Excel spreadsheet and email template.\nAre you sure you want to continue (Y/N)?\n")

    print("\n")

    if (input_value == "Y" or input_value == "y"):
        # Path to env keys
        PATH_ENV = Path(Path.cwd(), "envkeysfiles", ".env")
        # Loading enviornment variables
        load_dotenv(dotenv_path=PATH_ENV)

        # Other path constants
        PATH_XLSX = Path(Path.cwd(), "assets", "spreadsheet",
                         os.getenv("DATABASE_FILE_NAME"))
        PATH_GENERAL_EMAIL_TITLE = Path(Path.cwd(), "assets",
                                        "htmltemplates", os.getenv("GENERAL_EMAIL_TITLE_FILE_NAME"))
        PATH_GENERAL_EMAIL_BODY = Path(Path.cwd(), "assets",
                                       "htmltemplates", os.getenv("GENERAL_EMAIL_BODY_FILE_NAME"))
        PATH_PERSONAL_EMAIL_TITLE = Path(Path.cwd(), "assets",
                                         "htmltemplates", os.getenv("PERSONAL_EMAIL_TITLE_FILE_NAME"))
        PATH_PERSONAL_EMAIL_BODY = Path(Path.cwd(), "assets",
                                        "htmltemplates", os.getenv("PERSONAL_EMAIL_BODY_FILE_NAME"))
        PATH_EMAIL_ATTACHMENT = Path(Path.cwd(), "assets",
                                     "attachments", os.getenv("ATTACHMENT_FILE_NAME"))

        # Loading data from .xlsx file
        xlsx_file = Spreadsheet(PATH_XLSX)

        # Loading template from HTML file
        email_template_general = Emailtemplate(
            PATH_GENERAL_EMAIL_TITLE, PATH_GENERAL_EMAIL_BODY)
        email_template_personal = Emailtemplate(
            PATH_PERSONAL_EMAIL_TITLE, PATH_PERSONAL_EMAIL_BODY)
        email_templates = Templatescontainer(
            email_template_general, email_template_personal)

        # Loading email address finding details
        email_finder = Emailfinder(str(os.getenv("HUNTER_API_KEY")))

        # Load sending data emails
        gmail_send = Gmailsend(os.getenv("GMAIL_EMAIL"),
                               os.getenv("GMAIL_ALIAS"))

        # Loading bulk send for sending emails
        bulk_send = Bulksending(xlsx_file, gmail_send, email_finder,
                                email_templates, str(PATH_EMAIL_ATTACHMENT))

        # Sending emails
        bulk_send.sendmail()
        print("\nEmail sending completed.\n")
    else:
        print("\nDid not send any email\n")


if __name__ == '__main__':
    main()
