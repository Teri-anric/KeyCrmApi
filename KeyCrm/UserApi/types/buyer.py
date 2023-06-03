from typing import List, Optional

from pydantic import BaseModel


class Buyer(BaseModel):
    id: int
    company_id: int
    full_name: str
    phone: Optional[str]
    email: Optional[str]
    note: Optional[str]
    picture: Optional[str]
    image: Optional[str]
    orders_sum: str
    currency: str
    orders_count: int
    has_duplicates: int
    manager_id: Optional[int]
    deleted_at: Optional[str]
    created_at: str
    updated_at: str


class ClientsCompany(BaseModel):
    current_page: int
    data: List[Buyer]
    first_page_url: str
    from_: int = None
    last_page: int
    last_page_url: str
    next_page_url: Optional[str]
    path: str
    per_page: int
    prev_page_url: Optional[str]
    to: int
    total: int
