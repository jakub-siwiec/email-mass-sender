import yagmail


class Gmailsend():
    def __init__(self, user_email, email_to, email_subject, email_contents):
        self.user_email = user_email
        self.email_to = email_to
        self.email_subject = email_subject
        self.email_contents = email_contents

    def send(self):
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
