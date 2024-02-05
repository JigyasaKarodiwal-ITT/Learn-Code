from googleapiclient.errors import HttpError

class EmailMetrics:
    def __init__(self, gmailApiService, userId):
        self.gmailApiService = gmailApiService
        self.userId = userId

    def getEmailCount(self, labelId):
        try:
            response = self.gmailApiService.users().labels().get(userId=self.userId, id=labelId).execute()
            return response['messagesTotal']
        except HttpError as e:
            print(f"Error getting emails: {e}")
            return 0
