from typing import List

from pydantic import BaseModel, HttpUrl


class File(BaseModel):
    id: int
    file_name: str
    url: HttpUrl
    size: int
    extension: str
    original_file_name: str
    mime_type: str
    created_at: str
    updated_at: str


class ListFile(BaseModel):
    total: int
    current_page: int
    per_page: int
    data: List[File]
    first_page_url: HttpUrl
    last_page_url: HttpUrl
    next_page_url: HttpUrl
