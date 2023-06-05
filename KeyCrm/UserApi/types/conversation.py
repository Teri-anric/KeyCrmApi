from typing import List, Optional
from pydantic import BaseModel

class Message(BaseModel):
    """
    Represents a message.
    """

    id: int
    """
    The ID of the message.
    """

    conversation_id: int
    """
    The ID of the conversation.
    """

    type: str
    """
    The type of the message.
    """

    message_type: str
    """
    The type of the message content.
    """

    sender_id: Optional[int]
    """
    The ID of the sender.
    """

    message_body: str
    """
    The body/content of the message.
    """

    context: List[str]
    """
    The context of the message.
    """

    state: str
    """
    The state of the message.
    """

    error_message: Optional[str]
    """
    The error message associated with the message.
    """

    is_reply: bool
    """
    Indicates if the message is a reply.
    """

    external_id: str
    """
    The external ID of the message.
    """

    replied_message_id: Optional[int]
    """
    The ID of the replied message, if any.
    """

    attachments: List[str]
    """
    The attachments associated with the message.
    """

    delivered_at: Optional[str]
    """
    The delivery timestamp of the message.
    """

    reactions: List[str]
    """
    The reactions to the message.
    """

    is_read: int
    """
    Indicates if the message has been read.
    """

    created_at: str
    """
    The creation timestamp of the message.
    """

    updated_at: str
    """
    The last modification timestamp of the message.
    """

    deleted_at: Optional[str]
    """
    The deletion timestamp of the message, if deleted.
    """

    channel_driver: Optional[str]
    """
    The channel driver of the message.
    """

    channel_name: Optional[str]
    """
    The channel name of the message.
    """

    model: Optional[str]
    """
    The model type of the message.
    """

    reply_message: Optional[str]
    """
    The reply message content, if any.
    """