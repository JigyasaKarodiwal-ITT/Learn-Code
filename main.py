from GmailAPIAuthorization import GmailAPIAuthorization
from EmailMetrics import EmailMetrics
from CarbonEmissionCalculator import CarbonEmissionCalculator
from EmailAnalyzer import EmailAnalyzer

def main():
    token_path = 'token.json'

    gmail_api_authorization = GmailAPIAuthorization(token_path)
    gmail_api_service = gmail_api_authorization.authorize_gmail_api()

    email_metrics = EmailMetrics(gmail_api_service, 'apitesternew@gmail.com')
    carbon_emission_calculator = CarbonEmissionCalculator()

    email_analyzer = EmailAnalyzer(email_metrics, carbon_emission_calculator)
    email_analyzer.analyze_emails()

if __name__ == '__main__':
    main()
