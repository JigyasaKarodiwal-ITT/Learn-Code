import os
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google_auth_oauthlib.flow import InstalledAppFlow


class GmailAPIAuthorization:
    def __init__(self, tokenPath):
        self.tokenPath = tokenPath

    def authorizeGmailApi(self):
        mailCredentials = self._loadMailCredentials()

        if not mailCredentials or not mailCredentials.valid:
            if mailCredentials and mailCredentials.expired and mailCredentials.refresh_token:
                mailCredentials.refresh(Request())
            else:
                mailCredentials = self._obtainCredentials()

        return build('gmail', 'v1', credentials=mailCredentials)

    def _loadMailCredentials(self):
        mailCredentials = None
        if os.path.exists(self.tokenPath):
            mailCredentials = Credentials.from_authorized_user_file(self.tokenPath)
        return mailCredentials

    def _obtainCredentials(self):
        flow = InstalledAppFlow.from_client_secrets_file(
            'credentials.json', ['https://www.googleapis.com/auth/gmail.readonly'])
        mailCredentials = flow.run_local_server(port=0)

        with open(self.tokenPath, 'w') as token:
            token.write(mailCredentials.to_json())

        return mailCredentials
