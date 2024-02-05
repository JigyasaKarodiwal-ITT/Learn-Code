class EmailAnalyzer:
    def __init__(self, email_metrics, carbon_emission_calculator):
        self.email_metrics = email_metrics
        self.carbon_emission_calculator = carbon_emission_calculator

    def analyze_emails(self):
        user_id = 'apitesternew@gmail.com'
        inbox_mail_count = self.email_metrics.get_email_count('INBOX')
        sent_mail_count = self.email_metrics.get_email_count('SENT')
        spam_mail_count = self.email_metrics.get_email_count('SPAM')

        print(f'Inbox count: {inbox_mail_count}')
        print(f'Sent count: {sent_mail_count}')
        print(f'Spam count: {spam_mail_count}')

        total_emails = inbox_mail_count + sent_mail_count + spam_mail_count
        total_emission = self.carbon_emission_calculator.calculate_carbon_emission(total_emails)
        print(f'Estimated email carbon emission: {total_emission} kilograms of CO2')
