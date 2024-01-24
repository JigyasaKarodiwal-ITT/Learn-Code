def get_label_message_count(service, user_id, label_id):
    try:
        response = service.users().labels().get(userId=user_id, id=label_id).execute()
        return response['messagesTotal']
    except HttpError as e:
        print(f"Error getting emails: {e}")
        return 0