from datetime import datetime
from typing import List, Optional

from .base import ListResponse

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
    quantity: Optional[int]
    currency_code: Optional[str]
    min_price: Optional[float] = 0
    max_price: Optional[float] = 0
    weight: Optional[float] = None
    length: Optional[int] = None
    width: Optional[int] = None
    height: Optional[float] = None
    has_offers: bool = False
    is_archived: Optional[bool] = False
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
    price: Optional[float]
    purchased_price: Optional[float]
    weight: Optional[float]
    height: Optional[int]
    length: Optional[int]
    width: Optional[int]



class OfferResponse(ListResponse[Offer]):
    ...


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


class OfferStocksResponse(ListResponse[OfferStocks]):
    ...


class UpdateStocks(BaseModel):
    id: Optional[int]
    sku: Optional[str]
    quantity: int
