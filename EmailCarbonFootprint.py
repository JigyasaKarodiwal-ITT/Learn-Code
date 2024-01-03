import os
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google_auth_oauthlib.flow import InstalledAppFlow

def load_mail_credentials(token_path):
    mail_credentials = None
    if os.path.exists(token_path):
        mail_credentials = Credentials.from_authorized_user_file(token_path)

    return mail_credentials

def authorize_gmail_api(token_path):
    mail_credentials = load_mail_credentials(token_path)

    if not mail_credentials or not mail_credentials.valid:
        mail_credentials = refresh_or_obtain_credentials(token_path)

    return build('gmail', 'v1', credentials=mail_credentials)

def refresh_or_obtain_credentials(token_path):
    flow = InstalledAppFlow.from_client_secrets_file(
        'credentials.json', ['https://www.googleapis.com/auth/gmail.readonly'])
    mail_credentials = flow.run_local_server(port=0)

    with open(token_path, 'w') as token:
        token.write(mail_credentials.to_json())

    return mail_credentials

def get_label_message_count(service, user_id, label_id):
    try:
        response = service.users().labels().get(userId=user_id, id=label_id).execute()
        return response['messagesTotal']
    except HttpError as e:
        print(f"Error getting emails: {e}")
        return 0

def calculate_carbon_emission(email_count):
    carbon_emission_per_email = 0.02 
    total_emission = email_count * carbon_emission_per_email
    return total_emission

def main():
    token_path = 'token.json'
    gmail_api_service = authorize_gmail_api(token_path)
    user_id = 'apitesternew@gmail.com'

    inbox_mail_count = get_label_message_count(gmail_api_service, user_id, 'INBOX')
    sent_mail_count = get_label_message_count(gmail_api_service, user_id, 'SENT')
    spam_mail_count = get_label_message_count(gmail_api_service, user_id, 'SPAM')

    print(f'Inbox count: {inbox_mail_count}')
    print(f'Sent count: {sent_mail_count}')
    print(f'Spam count: {spam_mail_count}')

    total_emails = inbox_mail_count + sent_mail_count + spam_mail_count
    total_emission = calculate_carbon_emission(total_emails)
    print(f'Estimated email carbon emission: {total_emission} kilograms of CO2')

if __name__ == '__main__':
    main()
