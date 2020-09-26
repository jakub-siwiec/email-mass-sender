class Emailtemplate:
    def __init__(self, location_title, location_body):
        self.email_title_file = open(location_title, 'r')
        self.email_title_string = self.email_title_file.read()
        self.email_body_file = open(location_body, 'r')
        self.email_body_string = self.email_body_file.read()

    def get_template_title(self):
        return self.email_title_string

    def get_template_body(self):
        return self.email_body_string
