from datetime import datetime

from typing import List, Optional, Any
from pydantic import BaseModel, HttpUrl

from .base import ListResponse


class CustomFieldProduct(BaseModel):
    """
    Represents a custom field in the product.
    """

    id: int
    """
    The ID of the field in the system.
    """

    uuid: str
    """
    The external identifier of the field.
    Example: OR_1037
    """

    name: str
    """
    The name of the field.
    Example: Кличка
    """

    type: str
    """
    The type of the field.
    Possible values: link, select, switcher, float, number, textarea, text, date, datetime
    Example: text
    """

    value: Any
    """
    The value of the field. For select fields, it returns a string array.
    Example: Лорд
    """

class Product(BaseModel):
    """
    Represents a product with included fields.
    """

    id: int
    """
    The ID of the product.
    """

    name: str
    """
    The name of the product.
    Example: Iphone XS max 256gb
    """

    sku: Optional[str]
    """
    The SKU (stock keeping unit) of the product. Returns only if the product has no offers (has_offers == false).
    Example: 001-242
    """

    barcode: Optional[str]
    """
    The barcode of the product. Returns only if the product has no offers (has_offers == false).
    Example: 001-242
    """

    price: Optional[float]
    """
    The price of the product. Returns only if the product has no offers (has_offers == false).
    Example: 124.5
    """

    purchased_price: Optional[float]
    """
    The purchased price of the product. Returns only if the product has no offers (has_offers == false).
    Example: 124.5
    """

    description: str
    """
    The description of the product.
    """

    thumbnail_url: Optional[HttpUrl]
    """
    The URL of the product thumbnail image.
    Example: https://i.etsystatic.com/22591342/r/il/52142a/2285383547/il_570xN.2285383547_h8a2.jpg
    """

    quantity: float
    """
    The total quantity of the product or the sum of quantities for all product variants, if any.
    """

    currency_code: str
    """
    The currency code of the product.
    Example: UAH
    """

    min_price: Optional[float]
    """
    The minimum price of the product variants. If the product has no variants (has_offers == false), it will be equal to the product price.
    """

    max_price: Optional[float]
    """
    The maximum price of the product variants. If the product has no variants (has_offers == false), it will be equal to the product price.
    """

    weight: float
    """
    The default weight of the product.
    """

    length: float
    """
    The default length of the product.
    """

    width: float
    """
    The default width of the product.
    """

    height: float
    """
    The default height of the product in system units.
    """

    has_offers: bool
    """
    Indicates whether the product has variants.
    Example: false
    """

    is_archived: bool
    """
    Indicates whether the product is archived.
    Example: false
    """

    category_id: Optional[int]
    """
    The ID of the product category.
    """

    created_at: datetime
    """
    The creation date of the product in UTC format.
    Example: 2020-05-16 17:00:07
    """

    updated_at: datetime
    """
    The last update date of the product in UTC format.
    Example: 2020-05-16 17:00:07
    """

    custom_fields: List[CustomFieldProduct]
    """
    The custom fields in the product. Only returned if 'include=custom_fields' is specified.
    """

class ListProducts(ListResponse):
    data: List[Product]



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
    custom_fields: Optional[List[CustomFieldProduct]] = None
