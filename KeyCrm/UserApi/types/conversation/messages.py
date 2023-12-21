from pydantic import BaseModel
from typing import List, Optional
from .conversation_message import ConversationMessage


class CursorPage(BaseModel):
    direction: str
    target: str

class Cursor(BaseModel):
    current_page: CursorPage
    first_page: CursorPage
    last_page: CursorPage
    next_page: CursorPage
    previous_page: CursorPage

class MessageList(BaseModel):
    data: List[ConversationMessage]
    per_page: int
    total: int
    has_next: bool
    has_previous: bool
    first_page_url: Optional[str]
    last_page_url: Optional[str]
    next_page_url: Optional[str]
    prev_page_url: Optional[str]
    path: str
    cursor: Optional[Cursor]