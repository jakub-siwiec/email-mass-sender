import re


class Emailtemplate:
    def __init__(self, location_title, location_body):
        """Loading email templates for title and body from another files

        Args:
            location_title (string): Path to title html file
            location_body (string): Path to body html file
        """
        self.email_title_file = open(location_title, 'r')
        self.email_title_string = self.email_title_file.read()
        self.email_body_file = open(location_body, 'r')
        self.email_body_string = self.email_body_file.read()
        # Lists of strings between curly braces {{}}
        self.email_title_variables = re.findall(
            "(?<=\{{)(.*?)(?=\}})", self.email_title_string)
        self.email_body_variables = re.findall(
            "(?<=\{{)(.*?)(?=\}})", self.email_body_string)

    def get_template_title_variables(self):
        """ Get an array of variables in .html file for title. Variables are sorrounded by double curly braces e.g. {{variable}}.

        Returns:
            array: Array of the variables in the title file.
        """
        return self.email_title_variables

    def get_template_body_variables(self):
        """ Get an array of variables in .html file for body. Variables are sorrounded by double curly braces e.g. {{variable}}.

        Returns:
            array: Array of the variables in the body file.
        """

        return self.email_body_variables

    def get_template_title(self):
        """Template title getter.

        Returns:
            [string]: String of title
        """
        return self.email_title_string

    def get_template_body(self):
        """Template body getter. Recommended formatting in html.

        Returns:
            [string]: String of body
        """
        return self.email_body_string
