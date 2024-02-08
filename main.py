from GmailAPIAuthorization import GmailAPIAuthorization
from EmailMetrics import EmailMetrics
from CarbonEmissionCalculator import CarbonEmissionCalculator
from EmailAnalyzer import EmailAnalyzer

def main():
    tokenPath = 'token.json'
    
    gmailApiAuthorization = GmailAPIAuthorization(tokenPath)
    gmailApiService = gmailApiAuthorization.authorizeGmailApi()

    emailMetrics = EmailMetrics(gmailApiService, 'apitesternew@gmail.com')
    carbonEmissionCalculator = CarbonEmissionCalculator()

    emailAnalyzer = EmailAnalyzer(emailMetrics, carbonEmissionCalculator)
    emailAnalyzer.analyzeEmails()


if __name__ == '__main__':
    main()
