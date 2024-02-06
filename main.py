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