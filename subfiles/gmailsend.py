import yagmail


class Gmailsend():
    def __init__(self, user_email):
        """Gmail email sender. Constructor for initialising server connection and authentication

        Args:
            user_email (string): Email from which the message will be sent
        """
        self.user_email = user_email
        # initializing the server connection
        self.yag = yagmail.SMTP(user=self.user_email,
                                oauth2_file="oauth2_creds.json")

    def send(self, email_to, email_subject, email_contents, attachment_location):
        """Sending an email

        Args:
            email_to (string): Message receiver
            email_subject (string): Message title
            email_contents (string): Message content
            attachment_location (string): location of the attachment
        """
        try:
            # sending the email
            self.yag.send(to=email_to, subject=email_subject,
                          contents=email_contents, attachments=attachment_location)
            print("Email sent successfully")
        except:
            print("Error, email was not sent")
