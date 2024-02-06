def load_mail_credentials(token_path):
    mail_credentials = None
    if os.path.exists(token_path):
        mail_credentials = Credentials.from_authorized_user_file(token_path)
       
    return mail_credentials