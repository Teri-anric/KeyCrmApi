from typing import Optional, List

from pydantic import BaseModel


class Option(BaseModel):
    id: int
    field_id: int
    value: str


class CustomField(BaseModel):
    id: int
    name: str
    uuid: str
    model: str
    type: str
    required: bool
    position: int
    is_multiple: bool
    options: Optional[List[Option]] = None
