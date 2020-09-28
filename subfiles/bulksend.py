import math


def bulk_sending(xlsx_file, gmail_send, email_template, attachment_location, email_finder):
    """[summary]

    Args:
        xlsx_data ([type]): [description]
        gmail_send ([type]): [description]
        email_template ([type]): [description]
    """
    xlsx_data = xlsx_file.get_xlsx_data()

    for item in xlsx_data.iterrows():
        # Personalising the data passed to the email
        email_template_title = email_template.get_template_title().replace(
            "{company}", item[1].company)
        email_template_body = email_template.get_template_body().replace(
            "{first_name}", item[1].first_name).replace("{company}", item[1].company)

        print(item[1].email_address == item[1].email_address)
        # Email sending procedure with checking the email address to send
        # Checking whether the item is nan
        if (item[1].email_address == item[1].email_address):
            # When there is an email
            # Sending an email
            result = gmail_send.send(item[1].email_address, email_template_title,
                                     email_template_body, attachment_location)
            # Printing the result to the spreadsheet
            xlsx_file.add_to_row(item[0]+1, "Success" if result else "Fail")
        # When there is no email given
        elif (item[1].hunter == 1):
            # Checking the email in hunter
            email_finder.set_data(
                item[1].first_name, item[1].last_name, item[1].domain)
            email_address = email_finder.hunter_api
            if email_address == None:
                # There is no email in hunter we are trying to guess it
                for address in email_finder.email_guesser_list():
                    print("first: " + address)
                    gmail_send.send(address, email_template_title,
                                    email_template_body, attachment_location)
            else:
                # Sending an email
                result = gmail_send.send(email_address, email_template_title,
                                         email_template_body, attachment_location)
                # Printing the result to the spreadsheet
                xlsx_file.add_to_row(
                    item[0]+1, "Success" if result else "Fail")
        else:
            # We do not use hunter for email searching we are trying to guess it
            email_finder.set_data(
                item[1].first_name, item[1].last_name, item[1].domain)
            for address in email_finder.email_guesser_list():
                print("second: " + address)
                gmail_send.send(address, email_template_title,
                                email_template_body, attachment_location)


class Bulksending:
    def __init__(self, xlsx_file, gmail_send, email_finder, email_template, attachment_location):
        self.xlsx_file = xlsx_file
        self.xlsx_data = self.xlsx_file.get_xlsx_data()
        self.gmail_send = gmail_send
        self.email_finder = email_finder
        self.email_template = email_template
        self.attachment_location = attachment_location

    def __personalising_template_title(self, item):
        return self.email_template.get_template_title().replace("{company}", item[1].company)

    def __personalising_template_body(self, item):
        return self.email_template.get_template_body().replace("{first_name}", item[1].first_name).replace("{company}", item[1].company)

    def __no_email_address_loader(self, item):
        self.email_finder.set_data(
            item[1].first_name, item[1].last_name, item[1].domain)

    def __hunter_email_finder(self):
        return self.email_finder.hunter_api

    def __sending_guessed_emails(self, item):
        result = []
        email_template_title = self.__personalising_template_title(item)
        email_template_body = self.__personalising_template_body(item)
        for address in self.email_finder.email_guesser_list():
            result.append(self.gmail_send.send(address, email_template_title,
                                               email_template_body, self.attachment_location))
        return result

    def __sending_known_email(self, item, email_address):
        result = []
        email_template_title = self.__personalising_template_title(item)
        email_template_body = self.__personalising_template_body(item)
        result.append(self.gmail_send.send(email_address, email_template_title,
                                           email_template_body, self.attachment_location))
        return result

    def __print_results(self, item, result):
        if result.count(True) == len(result):
            self.xlsx_file.add_to_row(item[0]+1, "Success")
        elif result.count(False) == len(result):
            self.xlsx_file.add_to_row(item[0]+1, "Fail")
        else:
            self.xlsx_file.add_to_row(item[0]+1, "Some succeeded, some failed")

    def sendmail(self):
        for item in self.xlsx_data.iterrows():
            pass
