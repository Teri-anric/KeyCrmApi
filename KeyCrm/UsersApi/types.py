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

class FieldProducts:
    @staticmethod
    def get(item):
        return f"products.{item}"

    def __getattr__(self, item):
        self.get(item)

    primary_key = 'products.primary_key'
    name = 'products.name'
    description = 'products.description'
    currency_code = 'products.currency_code'
    category_name = 'products.category_name'
    thumbnail = 'products.thumbnail'
    weight = 'products.weight'
    length = 'products.length'
    height = 'products.height'
    width = 'products.width'

class FieldOffers:
    @staticmethod
    def get(item):
        return f"products.{item}"

    def __getattr__(self, item):
        self.get(item)

    id = 'offers.id'
    sku = 'offers.sku'
    barcode = 'offers.barcode'
    price = 'offers.price'
    purchased_price = 'offers.purchased_price'
    weight = 'offers.weight'
    length = 'offers.length'
    height = 'offers.height'
    width = 'offers.width'
    property_name = 'offers.property_name'
    property_value = 'offers.property_value'


