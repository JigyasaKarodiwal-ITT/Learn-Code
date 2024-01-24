def authorize_gmail_api(token_path):
    mail_credentials = load_mail_credentials(token_path)

    if not mail_credentials or not mail_credentials.valid:
        mail_credentials = refresh_or_obtain_credentials(token_path)

    return build('gmail', 'v1', credentials=mail_credentials)