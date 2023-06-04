from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime

class BuyerOrder(BaseModel):
    """
    Represents information about the buyer.
    """

    id: Optional[int]
    """
    The ID of the buyer in KeyCRM.
    """

    full_name: Optional[str]
    """
    The full name of the buyer.
    """

    email: Optional[str]
    """
    The email of the buyer.
    """

    phone: Optional[str]
    """
    The phone number of the buyer.
    """

    company_id: Optional[int]
    """
    The ID of the company associated with the buyer.
    """

    manager_id: Optional[int]
    """
    The ID of the manager associated with the buyer.
    """

class Shipping(BaseModel):
    """
    Represents information about the shipping.
    """

    delivery_service_id: Optional[int]
    """
    The ID of the delivery service in KeyCRM.
    """

    tracking_code: Optional[str]
    """
    The tracking code of the order.
    """

    shipping_status: Optional[str]
    """
    The shipping status of the order.
    """

    shipping_address_city: Optional[str]
    """
    The city of the shipping address.
    """

    shipping_address_country: Optional[str]
    """
    The country of the shipping address.
    """

    shipping_address_country_code: Optional[str]
    """
    The country code of the shipping address.
    """

    shipping_address_region: Optional[str]
    """
    The region of the shipping address.
    """

    shipping_address_zip: Optional[str]
    """
    The ZIP code of the shipping address.
    """

    shipping_secondary_line: Optional[str]
    """
    The additional address information.
    """

    shipping_receive_point: Optional[str]
    """
    The receive point of the order.
    """

    recipient_full_name: Optional[str]
    """
    The full name of the recipient (if different from the buyer).
    """

    recipient_phone: Optional[str]
    """
    The phone number of the recipient (if different from the buyer).
    """

    shipping_date_actual: Optional[str]
    """
    The actual shipping/delivery date.
    """

class Order(BaseModel):
    """
    Represents an order.
    """

    id: int
    """
    The ID of the order.
    """

    parent_id: Optional[int]
    """
    The ID of the parent order.
    """

    source_uuid: Optional[str]
    """
    The unique identifier of the order from the loaded source.
    """

    source_id: int
    """
    The ID of the source.
    """

    status_id: int
    """
    The ID of the order status.
    """

    status_group_id: int
    """
    The ID of the order status group.
    """

    grand_total: float
    """
    The final cost of the order.
    """

    promocode: Optional[str]
    """
    The promo code of the order.
    """

    total_discount: float
    """
    The total discount amount of the order.
    """

    expenses_sum: float
    """
    The total expenses amount of the order.
    """

    shipping_price: Optional[float]
    """
    The shipping cost of the order.
    """

    wrap_price: Optional[float]
    """
    The gift wrapping cost of the order.
    """

    taxes: Optional[float]
    """
    The total tax amount of the order.
    """

    manager_comment: Optional[str]
    """
    The manager's comment.
    """

    buyer_comment: Optional[str]
    """
    The buyer's comment.
    """

    gift_message: Optional[str]
    """
    The gift message.
    """

    is_gift: bool
    """
    Indicates if the order is marked as a gift.
    """

    payment_status: Optional[str]
    """
    The payment status of the order.
    """

    last_synced_at: str
    """
    The last synchronization date with the source in UTC format.
    """

    created_at: str
    """
    The creation date of the order in UTC format.
    """

    updated_at: str
    """
    The last modification date of the order in UTC format.
    """

    closed_at: Optional[str]
    """
    The closing date of the order in UTC format.
    """

    buyer: Optional[BuyerOrder]
    """
    Information about the buyer. Only returned if 'include=buyer' is specified.
    """

    products: Optional[List[dict]]
    """
    The list of products in the order.
    """

    manager: Optional[dict]
    """
    Information about the manager.
    """

    tags: Optional[List[dict]]
    """
    The list of tags associated with the order.
    """

    status: Optional[dict]
    """
    Information about the order status.
    """

    marketing: Optional[dict]
    """
    Information about the marketing.
    """

    payments: Optional[List[dict]]
    """
    The list of payments associated with the order.
    """

    shipping: Optional[Shipping]
    """
    Information about the shipping. Only returned if 'include=shipping' is specified.
    """

    expenses: Optional[List[dict]]
    """
    The list of expenses associated with the order.
    """

    custom_fields: Optional[List[dict]]
    """
    The list of custom fields in the order.
    """
