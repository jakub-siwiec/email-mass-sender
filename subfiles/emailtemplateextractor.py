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
