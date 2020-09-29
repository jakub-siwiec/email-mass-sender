# Enviornment variables file

File named *.env* with enviornment variables. Required enviornment variables for the complete functioning of the program:

```
// Email address from which emails are sent
GMAIL_EMAIL

// Alias (the name appearing in the mailbox as a sender instead of email address) for the emails sent
GMAIL_ALIAS

// A full name (including .xlsx extension) of Excel spreadsheet file
DATABASE_FILE_NAME

// A full name (including extension such as .pdf) of the attachment file
ATTACHMENT_FILE_NAME

// A full name (including .html extension) of the title template file
EMAIL_TITLE_FILE_NAME

// A full name (including .html extension) of the body template file
EMAIL_BODY_FILE_NAME

// Hunter API key which can be obtained from Hunter.io account
HUNTER_API_KEY
```

Keep in mind that for the correct functioning of the program you will also need `gmail_client_id` and `gmail_client_secret` for Google API authentication. They are stored in *oauth2_creds.json*.