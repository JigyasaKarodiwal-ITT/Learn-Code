def refresh_or_obtain_credentials(token_path):
    flow = InstalledAppFlow.from_client_secrets_file(
        'credentials.json', ['https://www.googleapis.com/auth/gmail.readonly'])
    mail_credentials = flow.run_local_server(port=0)

    with open(token_path, 'w') as token:
        token.write(mail_credentials.to_json())

    return mail_credentials