from KeyCrm.types.order import Order
from typing import List

class OrderMinix:
    def get_order(self, order_id: int, include: List[str] = None) -> Order:
        """
        Retrieves the order entity by the provided identifier.

        Args:
            order_id: The identifier of the order.
            include: A list of additional associations to include. Допустимі асоціації buyer, products.offer, manager, tags, status, marketing, payments, shipping.lastHistory, shipping.deliveryService, expenses, custom_fields

        Returns:
            An Order object containing the response data.
        """
        # Define the URL
        url = f'/order/{order_id}'

        params = {}
        if include:
            params = {
                'include': ','.join(include)  # Convert the list to a comma-separated string
            }

        return Order.parse_obj(self._get_request(url, params=params))
