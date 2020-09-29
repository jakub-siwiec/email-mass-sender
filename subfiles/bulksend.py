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

    def __personal_or_general_template(self, item):
        """ Chooses personal or general template. If 1 in Excel then then it is personal.

        Args:
            item (tuple): Tuple from pandas DataFrame.

        Returns:
            template object: Template object which is personal or general
        """
        if item[1].personal == 1 or item[1].personal == "1":
            return self.email_templates.personal()
        else:
            return self.email_templates.general()

    def __template_title_variable_personalisation(self, item):
        """ Personalising template title with the variables values.

        Args:
            item (tuple): Tuple from pandas DataFrame.

        Returns:
            string: Email template title
        """
        email_template_title = self.__personal_or_general_template(
            item).get_template_title()
        template_title_variables = self.__personal_or_general_template(
            item).get_template_title_variables()
        excel_headers_variables = self.xlsx_file.get_headers_list()

        # Getting common values in two arrays
        common_variables_list = list(set(template_title_variables).intersection(
            set(excel_headers_variables)))

        for variable in common_variables_list:
            email_template_title = email_template_title.replace(
                "{{" + str(variable) + "}}", item[1][str(variable)])

        return email_template_title

    def __template_body_variable_personalisation(self, item):
        """ Personalising template body with the variables values.

        Args:
            item (tuple): Tuple from pandas DataFrame.

        Returns:
            string: Email template body
        """

        email_template_body = self.__personal_or_general_template(
            item).get_template_body()
        template_body_variables = self.__personal_or_general_template(
            item).get_template_body_variables()
        excel_headers_variables = self.xlsx_file.get_headers_list()

        # Getting common values in two arrays
        common_variables_list = list(set(template_body_variables).intersection(
            set(excel_headers_variables)))

        for variable in common_variables_list:
            email_template_body = email_template_body.replace(
                "{{" + str(variable) + "}}", item[1][str(variable)])

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
        email_template_title = self.__template_title_variable_personalisation(
            item)
        email_template_body = self.__template_body_variable_personalisation(
            item)
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
        email_template_title = self.__template_title_variable_personalisation(
            item)
        email_template_body = self.__template_body_variable_personalisation(
            item)
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
