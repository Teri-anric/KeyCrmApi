from typing import List, Optional, Union, Dict, Any

from KeyCrm.types.offers import OfferResponse, Offer, UpdateOffer, OfferStocksResponse, UpdateStocks
from KeyCrm.utils import parse_filters

class OfferMinix:
    def get_offers(self, limit: int = 5, page: int = 1, include: Optional[str] = None, sort: Optional[str] = None,  filters: Optional[Dict[str, Union[str, list]]] = None) -> OfferResponse:
        url = "/offers"
        params = {'limit': limit, 'page': page}
        if include is not None:
            params['include'] = include
        if sort is not None:
            params['sort'] = sort
        if filters is not None:
            params.update(parse_filters(filters))

        return OfferResponse.parse_obj(self._get_request(url, params))

    def get_iter_all_offers(self, include: Optional[str] = None, sort: Optional[str] = None,  filters: Optional[Dict[str, Union[str, list]]] = None) -> List[Offer]:
        i = 1
        while 1:
            result = self.get_offers(limit=50, page=i, include=include, sort=sort, filters=filters)
            for offer in result.data:
                yield offer
            if not result.next_page_url:
               break
            i += 1


    def update_offer(self, offers: List[UpdateOffer]):
        url = "/offers"
        data = {"offers": [x.dict() for x in offers]}
        return self.put_request(url, data).get('status', False)

    def get_stocks(self, limit: int = 5, page: int = 1, filters: Optional[Dict[str, Union[str, list]]] = None):
        url = "/offers/stocks"
        params = {'limit': limit if limit else 5, 'page': page if page else 1}
        if filters is not None:
            params.update(parse_filters(filters))

        return OfferStocksResponse.parse_obj(self._get_request(url, params))

    def update_stocks(self, warehouse_id: int, stocks: List[UpdateStocks]):
        url = "/offers/stocks"
        data = {"warehouse_id": warehouse_id,  "stocks": [x.dict() for x in stocks]}
        return self._put_request(url, data).get('status', False)

