import requests


class Emailfinder:
    def __init__(self, hunter_API_key, first_name="", last_name="", domain=""):
        """Finds email address of a prospect

        Args:
            hunter_API_key (string): API key of Hunter
            first_name (string): First name of the prospect. Default is "". You can set it later.
            last_name (string): Last name of the prospect. Default is "". You can set it later.
            domain (string): Domain name of the prospect without http and www prefix, e.g. ey.com. Default is "". You can set it later.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.domain = domain
        self.hunter_API_key = str(hunter_API_key)

    def set_data(self, new_first_name, new_last_name, new_domain):
        """Setting data for the first and last name and domain.

        Args:
            new_first_name (string): Setting a first name.
            new_last_name (string): Setting a last name.
            new_domain (string): Setting a domain address (without http or www, e.g. ey.com).
        """
        self.first_name = new_first_name
        self.last_name = new_last_name
        self.domain = new_domain

    def hunter_api(self):
        """Searches for email in Hunter

        Returns:
            [string]: String email. If not found returns None
        """
        response = requests.get(
            "https://api.hunter.io/v2/email-finder?domain={}&first_name={}&last_name={}&api_key={}".format(self.domain, self.first_name, self.last_name, self.hunter_API_key))

        try:
            return response.json()['data']['email']
        except:
            return None

    def email_guesser_list(self):
        """Returns the list of emails based on the most common email address patterns

        Returns:
            [array]: Array of emails
        """
        self.first_name.replace(" ", "")
        self.last_name.replace(" ", "")
        email_list = []
        email_list.append("{}.{}@{}".format(self.first_name,
                                            self.last_name, self.domain).lower())
        email_list.append("{}{}@{}".format(self.first_name,
                                           self.last_name, self.domain).lower())
        email_list.append(
            "{}.{}@{}".format(self.first_name[0], self.last_name, self.domain).lower())
        email_list.append(
            "{}{}@{}".format(self.first_name[0], self.last_name, self.domain).lower())
        email_list.append("{}.{}@{}".format(self.first_name,
                                            self.last_name[0], self.domain).lower())
        email_list.append("{}{}@{}".format(self.first_name,
                                           self.last_name[0], self.domain).lower())
        email_list.append(
            "{}.{}@{}".format(self.first_name[0], self.last_name[0], self.domain).lower())
        email_list.append(
            "{}{}@{}".format(self.first_name[0], self.last_name[0], self.domain).lower())
        email_list.append("{}.{}@{}".format(self.last_name,
                                            self.first_name, self.domain).lower())
        email_list.append("{}{}@{}".format(self.last_name,
                                           self.first_name, self.domain).lower())
        email_list.append(
            "{}.{}@{}".format(self.last_name[0], self.first_name, self.domain).lower())
        email_list.append(
            "{}{}@{}".format(self.last_name[0], self.first_name, self.domain).lower())
        email_list.append("{}.{}@{}".format(self.last_name,
                                            self.first_name[0], self.domain).lower())
        email_list.append("{}{}@{}".format(self.last_name,
                                           self.first_name[0], self.domain).lower())
        email_list.append(
            "{}.{}@{}".format(self.last_name[0], self.first_name[0], self.domain).lower())
        email_list.append(
            "{}{}@{}".format(self.last_name[0], self.first_name[0], self.domain).lower())
        email_list.append("{}@{}".format(self.first_name, self.domain).lower())
        email_list.append("{}@{}".format(self.last_name, self.domain).lower())

        return email_list
