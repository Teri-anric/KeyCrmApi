from KeyCrm.UserApi.types.conversation import Message

class ConversationMinix:
    def message_by_client(self, client_id: int):
        url = f"conversations/messages/by_client/{client_id}"
        return [Message.parse_obj(obj) for obj in self._get_request(url)]

    def send_message(self, conversation_id: int, text: str):
        url = f"conversations/{conversation_id}/messages"
        params = {
            "attachments": [],
            "contex": [],
            "conversation_id": conversation_id,
            "is_email": False,
            "message_body": text,
            "reply_message": None,
            "types": "outgoing",
            "user_tags": []
        }
        return self._post_request(url, params=params)
