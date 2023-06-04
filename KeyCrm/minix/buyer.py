from KeyCrm.types.buyer import Buyer, ListBuyer
from KeyCrm.utils import parse_filters
from typing import Optional, List, Dict, Union

class BuyerMinix:
    def get_buyer(self, buyer_id: str, include: List[str] = None) -> Buyer:
        """
        Retrieves the buyer entity by the provided identifier.

        Args:
            buyer_id: The identifier of the buyer.
            include: List for additional associations. Valid associations are "manager", "shipping", "company", "custom_fields"

        Returns:
            A Buyer object containing the response data.
        """
        # Define the URL
        url = f'/buyer/{buyer_id}'

        # Set the query parameters
        params = {}
        if include:
            params['include'] = ','.join(include)  # Replace with the desired associations

        return Buyer.parse_obj(self._get_request(url, params=params))

    def get_buyers(self, limit: int = 15, page: int = 1, filters: Optional[Dict[str, Union[str, int, list]]] = None, include: List[str] = None) -> ListBuyer:
        """
        Retrieves a list of buyers.

        Args:
            limit: The maximum number of items in the paginated list (default: 15, maximum: 50).
            page: The page number.
            include: List for additional associations. Valid associations are "manager", "shipping", "company", "custom_fields"
            filters: Dict filter. key in "created_between", "updated_between", "buyer_id", "buyer_email", "buyer_phone".

        Returns:
            A list of Buyer objects containing the response data.
        """
        # Define the URL
        url = '/buyer'

        # Set the query parameters
        params = {
            'limit': limit,
            'page': page
        }
        params.update(parse_filters(filters))
        if include:
            params['include'] = ','.join(include)  # Convert the list to a comma-separated string

        return ListBuyer.parse_obj(self._get_request(url, params=params))
