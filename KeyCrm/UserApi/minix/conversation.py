from typing import Literal, Union, List, Dict

from KeyCrm.UserApi.types.conversation import Message, ConversationList, MessageList
from KeyCrm.utils import parse_filters


class ConversationMinix:
    def message_by_client(self, client_id: int):
        url = f"conversations/messages/by_client/{client_id}"
        return [Message.parse_obj(obj) for obj in self._get_request(url)]

    def send_message(self, conversation_id: int, text: str):
        return self._send_message(conversation_id, "outgoing", text)

    def _send_message(self, conversation_id: int, type_: str, text: str = None, attachments: List[Dict[str, str]] = []):
        url = f"conversations/{conversation_id}/messages"
        params = dict(
            attachments=attachments,
            context=[],
            conversation_id=conversation_id,
            is_email=False,
            message_body=text,
            reply_message=None,
            type=type_
        )
        return self._post_request(url, params=params)

    def send_message_note(self, conversation_id: int, text: str):
        return self._send_message(conversation_id, "notes", text)

    def get_unread_conversations(self) -> List[int]:
        """ Get all unread conversations
        :return: List id of the unread conversations
        """
        url = "conversations/unread"
        return self._get_request(url)

    def get_conversations(self, page: int = 1, assignee: Union[Literal["all", "my", "without_assignee"], int] = "my",
                          type_: Literal["opened", "closed", "all"] = "opened", unanswered: bool = False,
                          channels: Union[int, List[int]] = None, **filters) -> ConversationList:
        """ Get all conversations
        :param page: Page number (default = 1)
        :param assignee: The assignee of the conversation, id assignee or select "all", "my", "without_assignee"
        :param type_: Type of the conversation (default = opened)
        :param unanswered: Unanswered (default = None)
        :param channels: Channels ids
        :return:
        """
        url = f"conversations"
        filters.update(assignee=assignee, type=type_)
        if unanswered:
            filters["unanswered"] = True
        if channels is not None:
            filters["channels"] = channels
        params = dict(page=page, **parse_filters(filters, base="filters"))
        data = self._get_request(url, params=params)
        return ConversationList.parse_obj(data)

    def get_messages_by_conversation(self, conversation_id: int, page: int = 1, cursor: bool = True, after: str = None,
                                     before: str = None) -> MessageList:
        """ Get all messages
        :param after: The after of the conversation, id assignee or select
        :param before: The before of the conversation, id assignee or select
        :param conversation_id: The conversation id
        :param page: Page number (default = 1)
        :param cursor: Add cursor to the response (default = True)
        """
        url = f"conversations/{conversation_id}/messages"
        params = dict(page=page, cursor=cursor)
        if after is not None:
            params["after"] = after
        if before is not None:
            params["before"] = before
        data = self._get_request(url, params=params)
        return MessageList.parse_obj(data)
