from KeyCrm.types.order import Order
from typing import List

class OrderMinix:
    def get_order(self, order_id: str, include: List[str]) -> Order:
        """
        Retrieves the order entity by the provided identifier.

        Args:
            order_id: The identifier of the order.
            include: A list of additional associations to include.

        Returns:
            An Order object containing the response data.
        """
        # Define the URL
        url = f'/order/{order_id}'

        # Set the query parameters
        params = {
            'include': ','.join(include)  # Convert the list to a comma-separated string
        }

        return Order.parse_obj(self._get_request(url, params=params))
