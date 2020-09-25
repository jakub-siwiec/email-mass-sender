import yagmail


class Gmailsend():
    def __init__(self, user_email, email_to, email_subject, email_contents):
        """Object of email sending. It should generate oauth2_creds.json file for authentication.

        Args:
            user_email (string): Message sender
            email_to (string): Message receiver
            email_subject (string): Title of the email
            email_contents (string): Content of the email
        """
        self.user_email = user_email
        self.email_to = email_to
        self.email_subject = email_subject
        self.email_contents = email_contents

    def send(self):
        """Sending the email using yagmail library.
        """
        try:
            # initializing the server connection
            yag = yagmail.SMTP(user=self.user_email,
                               oauth2_file="oauth2_creds.json")
            # sending the email
            yag.send(to=self.email_to, subject=self.email_subject,
                     contents=self.email_contents)
            print("Email sent successfully")
        except:
            print("Error, email was not sent")
