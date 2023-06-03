from typing import List, Optional

from pydantic import BaseModel


class OfferProperty(BaseModel):
    name: str
    value: str


class Offer(BaseModel):
    sku: str
    price: str
    quantity: Optional[int]
    currency_code: Optional[str]
    weight: str
    length: str
    height: str
    width: str
    properties: List[OfferProperty]
    purchased_price: str


class CustomFieldValue(BaseModel):
    value: str
    field: dict
    field_id: int


class Product(BaseModel):
    id: Optional[int]
    name: str
    description: str
    thumbnail_url: Optional[str]
    currency_code: str
    weight: str
    length: str
    height: str
    width: str
    has_offers: bool
    offers: List[Offer]
    sku: Optional[str]
    barcode: Optional[str]
    price: str
    purchased_price: str
    publications: List[dict]
    properties_agg: dict
    category_id: Optional[int]
    custom_field_values: List[CustomFieldValue]
