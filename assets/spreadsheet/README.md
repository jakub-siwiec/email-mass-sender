# Spreadsheet file

The folder for Excel .xlsx spreadsheet file. The file name should match with `DATABASE_FILE_NAME` in *.env* file.

It should have columns *first_name*, *last_name*, *email_address*, *domain* (without any prefix, e.g. ey.com, microsoft.com). We also need the column *personal* which tells us whether we send an email to the specific person (e.g. Dustin Moskovitz) or to an unknown person (e.g. we begin with Dear Sir or Madam). If the value of personal column is 1 then the email based on personal template will be sent. If there will be anything else, the general email will be sent. The last column should be used for *Results*.