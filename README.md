# Email mass sender

A program which automatises sending bulk, personalised emails. 

**Purpose:** Personal purposes. Sometimes I need to send many similar emails and would like to do it quickly and to have fun at the same moment.

## Summary

### Technologies

Languages:

* Python

Package manager:

* Anaconda

### Setup

In order to authenticate with GMail, open [Google API Console](https://console.developers.google.com/). Then go to Credentials, click Create Credentials and choose OAuth Client ID (you might be asked to set up a project first). Go through the form to obtain Client ID and Client secret. It will be needed to login without a password while sending emails. When you will be sending emails for the first time *oauth2_creds.json* file will be created which will hold Client ID, Client secret and token. Don't share them with others. While logging in, you will be asked to authenticate with Google in your browser. 

For using [hunter.io](https://hunter.io/) you need to register there and obtain API key. You need to include it in the file named *.env* in *envkeysfiles* folder.

### How to use it

You need to:

* Create *.env* file in *envkeysfiles* folder with necessary keys
* Include Excel spreadsheet .xlsx file in *assets/spreadsheet* folder with the name matching appropriate key in *envkeysfiles.env* file and requirements for *xlsxreader* (described in *README* in the *spreadsheet* folder)
* Build email title and body templates in two separate files and .html format with the names matching the keys in *.env* file
* Paste attachments in the *attachments* folder matching the name in *.env* file

Then you fill Excel spreadsheet with your records and run the program. The results of the email sending will appear in the console and in the last column in Excel spreadsheet (use it for *Results*).

### How it works

The app will send emails with changing the variables in the templates for the record data to the email address in the Excel spreadsheet. If the cell with email_address is empty, the app will attempt to find an email address using the first name, last name and domain address through Hunter. If Hunter gives no results or the search limit in Hunter is used, the app will try to guess email address by sending out emails to addresses which are based on the most common professional email address patterns. In that case, the sender will receive multiple *Mail Delivery Subsystem 505 Access Denied* messages. However, there is a high chance that one email which was sent will not receive this message back; that will be the correct email address.