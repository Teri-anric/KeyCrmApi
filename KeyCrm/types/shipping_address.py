from pydantic import BaseModel
from typing import Optional

class ShippingAddress(BaseModel):
    """
    Represents shipping information.
    """

    address: Optional[str] = None
    """
    Delivery address.
    Nullable: true
    """

    additional_address: Optional[str] = None
    """
    Additional address information.
    """

    city: Optional[str] = None
    """
    City of delivery.
    Nullable: true
    Example: Kyiv
    """

    region: Optional[str] = None
    """
    Region or state of delivery.
    Nullable: true
    Example: Kyivska
    """

    zip_code: Optional[str] = None
    """
    Zip code of the delivery address.
    Nullable: true
    Example: 50000
    """

    country: Optional[str] = None
    """
    Country of delivery.
    Nullable: true
    Example: Ukraine
    """

    recipient_full_name: Optional[str] = None
    """
    Full name of the recipient (if different from the buyer).
    Nullable: true
    Example: Ann Doe
    """

    recipient_phone: Optional[str] = None
    """
    Phone number of the recipient (if different from the buyer).
    Nullable: true
    Example: +1 555-234-7777
    """

    warehouse_ref: Optional[str] = None
    """
    UUID reference of the warehouse for delivery (required with the delivery_service_id parameter - ID of the delivery service in CRM).
    Nullable: true
    Example: 1ec09d2e-e1c2-11e3-8c4a-0050568002cf
    """
