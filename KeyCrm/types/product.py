from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel


class ShortCustomField(BaseModel):
    id: int
    uuid: str
    name: str
    type: str
    value: str


class Product(BaseModel):
    id: int
    name: str
    sku: Optional[str] = None
    barcode: Optional[str] = None
    price: Optional[float] = None
    purchased_price: Optional[float] = None
    description: Optional[str]
    thumbnail_url: Optional[str]
    quantity: int
    currency_code: str
    min_price: Optional[float]
    max_price: Optional[float]
    weight: Optional[float]
    length: Optional[float]
    width: Optional[float]
    height: Optional[float]
    has_offers: bool
    is_archived: bool
    category_id: Optional[int]
    created_at: datetime
    updated_at: datetime
    custom_fields: Optional[List[ShortCustomField]]


class ProductCreateRequest(BaseModel):
    name: str
    description: Optional[str] = None
    pictures: Optional[List[str]] = None
    currency_code: Optional[str] = None
    sku: Optional[str] = None
    barcode: Optional[str] = None
    price: Optional[float] = None
    purchased_price: Optional[float] = None
    weight: Optional[float] = None
    length: Optional[float] = None
    height: Optional[float] = None
    category_id: Optional[int] = None
    custom_fields: Optional[List[ShortCustomField]] = None


class ProductsResponse(BaseModel):
    total: int
    current_page: int
    per_page: int
    data: List[Product]
    first_page_url: str
    last_page_url: str
    next_page_url: Optional[str]


class Category(BaseModel):
    id: int
    name: str
    parent_id: int


class CategoriesResponse(BaseModel):
    total: int
    current_page: int
    per_page: int
    data: List[Category]
    first_page_url: str
    last_page_url: str
    next_page_url: Optional[str]
