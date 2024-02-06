import os
import base64
import google.auth
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import requests
from google_auth_oauthlib.flow import InstalledAppFlow

def gmail_api_authorization():
    mail_credentials = None
    token_path = 'token.json'
    if os.path.exists(token_path):
        mail_credentials = Credentials.from_authorized_user_file(token_path)

    if not mail_credentials or not mail_credentials.valid:
        if mail_credentials and mail_credentials.expired and mail_credentials.refresh_token:
            mail_credentials.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
              'credentials.json', ['https://www.googleapis.com/auth/gmail.readonly'] )
            mail_credentials = flow.run_local_server(port=0)
        with open(token_path, 'w') as token:
            token.write(mail_credentials.to_json())
    return build('gmail', 'v1', credentials=mail_credentials)

def get_email_count(service, user_id, label_id):
    try:
        response = service.users().labels().get(userId=user_id, id=label_id).execute()
        return response['messagesTotal']
    except HttpError as e:
        print(f"Error getting emails: {e}")
        return 0
      
def amount_of_carbon_emission(email_count):
    carbon_emission_per_email = 0.02 
    total_emission = email_count * carbon_emission_per_email
    return total_emission

def main():
  gmail_api_service = gmail_api_authorization()
  user_id = 'apitesternew@gmail.com'

  inbox_mail_count = get_email_count(gmail_api_service, user_id, 'INBOX')
  sent_mail_count = get_email_count(gmail_api_service, user_id, 'SENT')
  spam_mail_count = get_email_count(gmail_api_service, user_id, 'SPAM')

  print(f'Inbox count: {inbox_mail_count}')
  print(f'Sent count: {sent_mail_count}')
  print(f'Spam count: {spam_mail_count}')

  total_emails = inbox_mail_count + sent_mail_count + spam_mail_count
  total_emission = amount_of_carbon_emission(total_emails)
  print(f'Estimated email carbon emission: {total_emission} kilograms of CO2')

if __name__ == '__main__':
  main()
