from typing import List, Optional, Union
from pydantic import BaseModel

from .conversation_message import ConversationMessage


class Contact(BaseModel):
    id: int
    full_name: str
    email: Optional[str]
    phone: Optional[str]
    social_name: str
    social_id: str
    picture: Optional[str]
    additional_details: List[str]

class AssignedTo(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str
    username: str
    role_id: int
    avatar_id: Optional[int]
    is_hidden: int
    is_owner: bool
    last_logged_at: str
    full_name: str
    is_bot: bool

class Channel(BaseModel):
    id: int
    driver: str
    name: str
    default_source_id: Optional[int]
    external_id: str
    is_public: bool
    is_active: bool
    pipeline_id: Optional[int]
    settings: dict
    driver_type: str
    roles: List[Union[str, dict]]


class Conversation(BaseModel):
    id: int
    channel_id: int
    assigned_user_id: Optional[int]
    contact_id: int
    contact_username: str
    comment: Optional[str]
    unread_count: int
    is_spam: bool
    external_id: str
    updated_timestamp: str
    archived_at: Optional[str]
    delayed_till: Optional[str]
    muted_at: Optional[str]
    created_at: str
    updated_at: str
    deleted_at: Optional[str]
    contact: Contact
    assigned_to: Optional[AssignedTo]
    channel: Channel
    last_message: ConversationMessage

class ConversationList(BaseModel):
    current_page: int
    data: List[Conversation]
    first_page_url: str
    # from_: int  # 'from' is a reserved keyword, so use 'from_'
    last_page: int
    last_page_url: str
    links: List[dict]
    next_page_url: Optional[str]
    path: str
    per_page: int
    prev_page_url: Optional[str]
    to: int
    total: int
