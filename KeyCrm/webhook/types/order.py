from pydantic import BaseModel
from typing import Optional, List

from .base import BaseEvent

class OrderStatusChangeContext(BaseModel):
    id: int
    source_uuid: Optional[str]
    status_on_source: Optional[str]
    source_id: int
    client_id: int
    grand_total: int
    total_discount: int
    expenses_sum: int
    discount_amount: int
    discount_percent: int
    shipping_price: Optional[str]
    taxes: Optional[str]
    fiscal_result: List[str]
    fiscal_status: Optional[str]
    manager_id: int
    status_group_id: int
    status_id: int
    status_changed_at: str
    parent_id: Optional[str]
    manager_comment: Optional[str]
    client_comment: Optional[str]
    is_gift: bool
    promocode: Optional[str]
    wrap_price: Optional[str]
    gift_wrap: bool
    payment_status: str
    gift_message: Optional[str]
    last_synced_at: Optional[str]
    created_at: str
    updated_at: str
    closed_at: Optional[str]
    deleted_at: Optional[str]
    ordered_at: str
    payments_total: int
    is_expired: bool
    has_reserves: bool

class OrderStatusChangeEvent(BaseEvent):
    event = "order.change_order_status"
    context: OrderStatusChangeContext