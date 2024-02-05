from googleapiclient.errors import HttpError

class EmailMetrics:
    def __init__(self, gmail_api_service, user_id):
        self.gmail_api_service = gmail_api_service
        self.user_id = user_id

    def get_email_count(self, label_id):
        try:
            response = self.gmail_api_service.users().labels().get(userId=self.user_id, id=label_id).execute()
            return response['messagesTotal']
        except HttpError as e:
            print(f"Error getting emails: {e}")
            return 0
