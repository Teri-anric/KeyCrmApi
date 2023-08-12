from typing import List, Optional, Union, Dict, Any

from KeyCrm.types.product import ListProducts, Product, CustomFieldProduct
from KeyCrm.types.category import Category, ListCategories
from KeyCrm.utils import parse_filters

from KeyCrm.exceptions import NotFound


class ProductMinix:
    def get_products(self, limit: int = 15, page: int = 1, include: List[str] = None,
                     filters: Dict[str, Any] = None) -> ListProducts:
        url = "/products"
        params = {'limit': limit if limit else 15, 'page': page if page else 1}
        if include is not None:
            params['include'] = ",".join(include)
        if filters is not None:
            params.update(parse_filters(filters))

        return ListProducts.parse_obj(self._get_request(url, params))

    def get_product(self, product_id: Union[int, str], include: List[str] = None) -> Optional[Product]:
        url = f"/products/{product_id}"
        params = {} if include is None else {'include': ",".join(include)}
        try:
            return Product.parse_obj(self._get_request(url, params))
        except NotFound:
            return None

    def create_product(self, name: str, description: Optional[str] = None, pictures: Optional[List[str]] = None,
                       currency_code: Optional[str] = None, sku: Optional[str] = None, barcode: Optional[str] = None,
                       price: Optional[float] = None, purchased_price: Optional[float] = None,
                       weight: Optional[float] = None, width: Optional[float] = None,
                       length: Optional[float] = None, height: Optional[float] = None,
                       category_id: Optional[int] = None, custom_fields: Optional[CustomFieldProduct] = None
                       ):
        url = "/products"
        request_data = ProductCreateRequest(
            name=name,
            description=description,
            pictures=pictures,
            currency_code=currency_code,
            sku=sku,
            barcode=barcode,
            price=price,
            purchased_price=purchased_price,
            weight=weight,
            length=length,
            height=height,
            category_id=category_id,
            custom_fields=custom_fields
        )
        self._post_request(url, request_data.dict())

    def get_categories(self, limit: int = 15, page: int = 1, filters: Optional[Dict[str, Union[str, list]]] = None) -> ListCategories:
        url = "/products/categories"
        params = {'limit': limit, 'page': page}
        if filters is not None:
            params.update(parse_filters(filters))

        return ListCategories.parse_obj(self._get_request(url, params))

    def create_category(self, name: str, parent_id: Optional[int] = None) -> Category:
        url = "/products/categories"
        params = {'name': name, parent_id: 'parent_id'}
        return Category.parse_obj(self._post_request(url, params))
