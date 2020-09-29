# Template files

The folder for two kinds (general and personal) of two separate templates (email title and email body). Their names should match `GENERAL_EMAIL_TITLE_FILE_NAME`, `GENERAL_EMAIL_BODY_FILE_NAME`, `PERSONAL_EMAIL_TITLE_FILE_NAME`, `PERSONAL_EMAIL_BODY_FILE_NAME` from *.env* file.

General template should be used for sending emails to an unknown recipient (e.g. beginning with Dear Sir or Madam)) and personal to a known recipient (e.g. beginning with Dear John).

Standard and custom variables should be enclosed in curly braces {{}} (e.g. *{{variable}}*).

Write and save files in .html format.