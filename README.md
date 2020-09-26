# Email mass sender

A program which automatises sending bulk, personalised emails. 

**Purpose:** Personal purposes. Sometimes I need to send many similar emails and would like to do it quickly.

## Summary

### Technologies

Languages:

* Python

Package manager:

* Anaconda

### Methods

### Setup

In order to authenticate with GMail, open [Google API Console](https://console.developers.google.com/). Then go to Credentials, click Create Credentials and choose OAuth Client ID (you might be asked to set up a project first). Go through the form to obtain Client ID and Client secret. It will be needed to login without a password while sending emails. When you will be sending emails for the first time *oauth2_creds.json* file will be created which will hold Client ID, Client secret and token. Don't share them with others. While logging in, you will be asked to authenticate with Google in your browser. 