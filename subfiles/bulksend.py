def bulk_sending(xlsx_data, gmail_send, email_template, attachment_location):
    """[summary]

    Args:
        xlsx_data ([type]): [description]
        gmail_send ([type]): [description]
        email_template ([type]): [description]
    """
    for item in xlsx_data.iterrows():
        # Personalising the data passed to the email
        email_template_title = email_template.get_template_title()
        email_template_body = email_template.get_template_body().replace(
            "{first_name}", item[1].first_name).replace("{email_address}", item[1].email_address)
        # Sending an email
        gmail_send.send(item[1].email_address, email_template_title,
                        email_template_body, attachment_location)
