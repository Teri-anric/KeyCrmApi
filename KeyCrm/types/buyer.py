from pydantic import BaseModel
from typing import List, Optional, Any

from .base import ListResponse
from .shipping_address import ShippingAddress
from .meneger import Manager
from .company import Company

class CustomFieldBuyer(BaseModel):
    """
    Represents a custom field for a buyer.
    """

    uuid: str
    """
    External identifier of the field.
    Example: OR_1037
    """

    value: Any
    """
    Value of the field. For fields with type 'select' (list/multiselect), pass an array of strings.
    Example: Лорд
    """

class Buyer(BaseModel):
    """
    Represents a buyer with included data.
    """

    id: int
    """
    Identifier of the buyer.
    Example: 22
    """

    full_name: str
    """
    Full name of the buyer.
    Nullable: false
    Example: John Doe
    """

    email: Optional[List[str]] = None
    """
    Email addresses of the buyer.
    Nullable: true
    Example: ["john.doe@mail.app", "john.doe2@mail.app"]
    """

    phone: Optional[List[str]] = None
    """
    Phone numbers of the buyer.
    Nullable: true
    Example: ["+1 555-234-1234", "+1 555-234-7777"]
    """

    note: Optional[str] = None
    """
    Note about the buyer.
    Nullable: true
    Example: Примітка
    """

    company: Optional[Company] = None
    """
    Information about the buyer's company. Only returned if include="company" is specified.
    """

    manager: Optional[Manager] = None
    """
    Information about the buyer's manager. Only returned if include="manager" is specified.
    """

    shipping: Optional[List[ShippingAddress]] = None
    """
    Information about delivery addresses. Only the filled ones are returned if include="shipping" is specified.
    """

    custom_fields: List[CustomFieldBuyer]
    """
    Custom fields for the buyer. Only the filled ones are returned if include="custom_fields" is specified.
    """

    created_at: Optional[str] = None
    """
    Creation date of the buyer in UTC format.
    Example: 2020-05-16 17:00:07
    """

    updated_at: Optional[str] = None
    """
    Last updated date of the buyer in UTC format.
    Example: 2020-05-16 17:00:07
    """

class ListBuyer(ListResponse):
    """
    An array of buyers in the response from the server
    """

    data: List[Buyer]
    """
    List for buyers
    """