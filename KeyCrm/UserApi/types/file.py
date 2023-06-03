from datetime import datetime

from pydantic import BaseModel


class FileData(BaseModel):
    directory: str
    file_name: str
    size: int
    hash: str
    original_file_name: str
    extension: str
    mime_type: str
    expired_at: dict
    disk: str
    updated_at: datetime
    created_at: datetime
    id: int
    url: str
    name: str
    full_path: str
    thumbnail: str
    original_file_hash: str = None
