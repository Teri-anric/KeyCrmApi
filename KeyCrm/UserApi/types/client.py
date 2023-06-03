from typing import List, Optional

from pydantic import BaseModel


class Profile(BaseModel):
    id: int
    client_id: int
    field: str
    value: str


class Client(BaseModel):
    id: int
    company_id: Optional[int]
    full_name: Optional[str]
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
    leads_count: int
    leads_sum: str
    profiles: List[Profile]
    custom_field_values: List[dict]
    shipping_addresses: List[dict]
