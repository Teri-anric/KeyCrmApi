from typing import Optional, Dict

from KeyCrm.UserApi.types.conversation import BaseMessage


class ConversationMessage(BaseMessage):
    subject: Optional[str]
    context: Optional[Dict[str, str]]
