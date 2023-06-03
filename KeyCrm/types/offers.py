from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel


class Property(BaseModel):
    name: str
    value: str


class ShortProduct(BaseModel):
    id: int
    name: str
    sku: Optional[str]
    barcode: Optional[str]
    description: Optional[str]
    thumbnail_url: Optional[str]
    quantity: int
    currency_code: str
    min_price: float
    max_price: float
    weight: float
    length: int
    width: int
    height: float
    has_offers: bool
    is_archived: bool
    category_id: Optional[int]
    created_at: datetime
    updated_at: datetime
    properties_agg: dict
    # custom_fields: Optional[List[ShortCustomField]]


class Offer(BaseModel):
    id: int
    product_id: int
    sku: Optional[str]
    barcode: Optional[str]
    price: float
    purchased_price: float
    quantity: int
    weight: Optional[float]
    length: Optional[float]
    width: Optional[float]
    height: Optional[float]
    product: Optional[ShortProduct]
    properties: Optional[List[Property]]


class UpdateOffer(BaseModel):
    id: Optional[int]
    sku: Optional[str]
    price: float
    purchased_price: float
    weight: float
    height: int
    length: int
    width: int


class OfferResponse(BaseModel):
    total: int
    current_page: int
    per_page: int
    data: List[Offer]
    first_page_url: str
    last_page_url: str
    next_page_url: Optional[str]


class Warehouse(BaseModel):
    id: int
    name: str
    quantity: int
    reserve: int


class OfferStocks(BaseModel):
    id: int
    sku: str
    price: float
    purchased_price: float
    quantity: int
    reserve: int
    warehouse: Optional[List[Warehouse]]


class OfferStocksResponse(BaseModel):
    total: int
    current_page: int
    per_page: int
    data: List[OfferStocks]
    first_page_url: str
    last_page_url: str
    next_page_url: Optional[str]


class UpdateStocks(BaseModel):
    id: Optional[int]
    sku: Optional[str]
    quantity: int
