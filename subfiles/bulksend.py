
class Bulksending:
    def __init__(self, xlsx_file, gmail_send, email_finder, email_templates, attachment_location=None):
        """ Sending bulk emails class

        Args:
            xlsx_file (Spreadsheet object): Spreadsheet object.
            gmail_send (Gmailsend object): Gmailsend object.
            email_finder (Email finder object): Emailfinder object.
            email_templates (Templatescontainer object): Templatescontainer object
            attachment_location (string, optional): String path to the attachment. Defaults to None.
        """
        self.xlsx_file = xlsx_file
        self.xlsx_data = self.xlsx_file.get_xlsx_data()
        self.gmail_send = gmail_send
        self.email_finder = email_finder
        self.email_templates = email_templates
        self.attachment_location = attachment_location

    def __personalising_template_title(self, item):
        """ Choosing right template and replacing the variables in the title template.

        Args:
            item (tuple): Tuple from pandas DataFrame.

        Returns:
            string: Final title template text.
        """
        email_template_title = ""
        print(item[1].personal)

        if item[1].personal == 1 or item[1].personal == "1":
            email_template_title = self.email_templates.personal(
            ).get_template_title().replace("{company}", item[1].company)
        else:
            email_template_title = self.email_templates.general(
            ).get_template_title().replace("{company}", item[1].company)

        return email_template_title

    def __personalising_template_body(self, item):
        """ Choosing right template and replacing the variables in the body template.

        Args:
            item (tuple): Tuple from pandas DataFrame.

        Returns:
            string: Final body template text.
        """
        email_template_body = ""

        if item[1].personal == 1 or item[1].personal == "1":
            email_template_body = self.email_templates.personal(
            ).get_template_body().replace("{first_name}", item[1].first_name).replace("{company}", item[1].company)
        else:
            email_template_body = self.email_templates.general(
            ).get_template_body().replace("{company}", item[1].company)

        return email_template_body

    def __is_email_not_nan(self, item):
        """ Checking whether email_address field in Excel spreadsheet is empty (nan).

        Args:
            item (tuple): Tuple from pandas DataFrame.

        Returns:
            boolean: True if the field is filled, False if the field is empty.
        """
        return item[1].email_address == item[1].email_address

    def __no_email_address_loader(self, item):
        """ Loading email_finder with the data for email address generation.

        Args:
            item (tuple): Tuple from pandas DataFrame.
        """
        self.email_finder.set_data(
            item[1].first_name, item[1].last_name, item[1].domain)

    def __hunter_email_finder(self):
        """ Getting the result of the search of hunter.io

        Returns:
            string: Address if address found, None if address not found or something went wrong with Hunter.
        """
        return self.email_finder.hunter_api()

    def __sending_known_email(self, item, email_address):
        """ Sending an email to one specific email address without guessing.

        Args:
            item (tuple): Tuple from pandas DataFrame.
            email_address (string): Email address

        Returns:
            array: Array of boolean values. True if email sent successfully, False if email sending failed.
        """
        result = []
        email_template_title = self.__personalising_template_title(item)
        email_template_body = self.__personalising_template_body(item)
        result.append(self.gmail_send.send(email_address, email_template_title,
                                           email_template_body, self.attachment_location))
        return result

    def __sending_guessed_emails(self, item):
        """ Sending emails from guessing list email generator.

        Args:
            item (tuple): Tuple from pandas DataFrame.

        Returns:
            array: Array of boolean values. True if email sent successfully, False if email sending failed.
        """
        result = []
        email_template_title = self.__personalising_template_title(item)
        email_template_body = self.__personalising_template_body(item)
        for address in self.email_finder.email_guesser_list():
            result.append(self.gmail_send.send(address, email_template_title,
                                               email_template_body, self.attachment_location))
        return result

    def __print_results(self, item, result):
        """ Printing the result of the email sending to the cell in the last column of the current row in Excel spreadsheet.

        Args:
            item (tuple): Tuple from pandas DataFrame.
            result (array): Array of booleans with the results of email sending.
        """
        if result.count(True) == len(result):
            self.xlsx_file.add_to_row(item[0]+1, "Success")
        elif result.count(False) == len(result):
            self.xlsx_file.add_to_row(item[0]+1, "Fail")
        else:
            self.xlsx_file.add_to_row(item[0]+1, "Some succeeded, some failed")

    def sendmail(self):
        """ Sending email method.
        """
        for item in self.xlsx_data.iterrows():
            if (self.__is_email_not_nan(item)):
                result = self.__sending_known_email(
                    item, item[1].email_address)
                self.__print_results(item, result)
            else:
                self.__no_email_address_loader(item)
                hunter_email = self.__hunter_email_finder()
                if (hunter_email == None):
                    result = self.__sending_guessed_emails(item)
                    self.__print_results(item, result)
                else:
                    result = self.__sending_known_email(item, hunter_email)
                    self.__print_results(item, result)
