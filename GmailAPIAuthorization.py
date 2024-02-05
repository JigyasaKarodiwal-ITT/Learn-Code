import os
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google_auth_oauthlib.flow import InstalledAppFlow

class GmailAPIAuthorization:
    def __init__(self, token_path):
        self.token_path = token_path

    def authorize_gmail_api(self):
        mail_credentials = self._load_mail_credentials()

        if not mail_credentials or not mail_credentials.valid:
            if mail_credentials and mail_credentials.expired and mail_credentials.refresh_token:
                mail_credentials.refresh(Request())
            else:
                mail_credentials = self._obtain_credentials()

        return build('gmail', 'v1', credentials=mail_credentials)

    def _load_mail_credentials(self):
        mail_credentials = None
        if os.path.exists(self.token_path):
            mail_credentials = Credentials.from_authorized_user_file(self.token_path)
        return mail_credentials

    def _obtain_credentials(self):
        flow = InstalledAppFlow.from_client_secrets_file(
            'credentials.json', ['https://www.googleapis.com/auth/gmail.readonly'])
        mail_credentials = flow.run_local_server(port=0)

        with open(self.token_path, 'w') as token:
            token.write(mail_credentials.to_json())

        return mail_credentials
