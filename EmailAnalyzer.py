class EmailAnalyzer:
    def __init__(self, emailMetrics, carbonEmissionCalculator):
        self.emailMetrics = emailMetrics
        self.carbonEmissionCalculator = carbonEmissionCalculator

    def analyzeEmails(self):
        userId = 'apitesternew@gmail.com'
        inboxMailCount = self.emailMetrics.getEmailCount('INBOX')
        sentMailCount = self.emailMetrics.getEmailCount('SENT')
        spamMailCount = self.emailMetrics.getEmailCount('SPAM')

        print(f'Inbox count: {inboxMailCount}')
        print(f'Sent count: {sentMailCount}')
        print(f'Spam count: {spamMailCount}')

        totalEmails = inboxMailCount + sentMailCount + spamMailCount
        totalEmission = self.carbonEmissionCalculator.calculateCarbonEmission(totalEmails)
        print(f'Estimated email carbon emission: {totalEmission} kilograms of CO2')
