from .types.order import OrderStatusChangeEvent
from .types.base import BaseEvent

def parse_request(data: dict) -> Optional[Union[OrderStatusChangeEvent, BaseEvent]]:
    event = data.get('event', None)
    if not event:
        return None
    if event == 'order.change_order_status':
        return OrderStatusChangeEvent.parse_obj(data)
    return BaseEvent.parse_obj(data)
