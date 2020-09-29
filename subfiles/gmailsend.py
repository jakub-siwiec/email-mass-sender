import yagmail


class Gmailsend():
    def __init__(self, user_email, alias_name):
        """Gmail email sender. Constructor for initialising server connection and authentication

        Args:
            user_email (string): Email from which the message will be sent
            alias_name (string): Alias (the name that appears in the receiver inbox) of your mail
        """
        self.user_email = user_email
        # initializing the server connection
        self.yag = yagmail.SMTP(user={self.user_email: alias_name},
                                oauth2_file="oauth2_creds.json")

    def send(self, email_to, email_subject, email_contents, attachment_location=None):
        """Sending an email

        Args:
            email_to (string): Message receiver
            email_subject (string): Message title
            email_contents (string): Message content
            attachment_location (string): location of the attachment. Default None.
        """
        try:
            # sending the email
            self.yag.send(to=email_to, subject=email_subject,
                          contents=email_contents, attachments=attachment_location)
            print("Email to " + email_to + " sent successfully")
            return True
        except:
            print("Error, email to " + email_to + " was not sent")
            return False
