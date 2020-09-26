def bulk_sending(xlsx_file, gmail_send, email_template, attachment_location):
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
        # Sending an email
        result = gmail_send.send(item[1].email_address, email_template_title,
                                 email_template_body, attachment_location)
        # Printing the result to the spreadsheet
        xlsx_file.add_to_row(item[0]+1, "Success" if result else "Fail")
