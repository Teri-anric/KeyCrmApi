from typing import List, Optional, Union, Dict, Any

from KeyCrm.types.product import ProductsResponse, ProductCreateRequest, ShortCustomField, Product, CategoriesResponse, \
    Category
from KeyCrm.utils import parse_filters


class ProductMinix:
    def get_products(self, limit: int = 15, page: int = 1, include: Optional[str] = None,
                     filters: Dict[str, Any] = None) -> ProductsResponse:
        url = "/products"
        params = {'limit': limit if limit else 15, 'page': page if page else 1}
        if include is not None:
            params['include'] = include
        if filters is not None:
            params.update(parse_filters(filters))

        return ProductsResponse.parse_obj(self._get_request(url, params))

    def get_product(self, product_id: Union[int, str], include: Optional[str] = None):
        url = f"/products/{product_id}"
        params = {} if include is None else {'include': include}
        Product.parse_obj(self._get_request(url, params))

    def create_product(self, name: str, description: Optional[str] = None, pictures: Optional[List[str]] = None,
                       currency_code: Optional[str] = None, sku: Optional[str] = None, barcode: Optional[str] = None,
                       price: Optional[float] = None, purchased_price: Optional[float] = None,
                       weight: Optional[float] = None, width: Optional[float] = None,
                       length: Optional[float] = None, height: Optional[float] = None,
                       category_id: Optional[int] = None, custom_fields: Optional[ShortCustomField] = None
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

    def get_categories(self, limit: int = 15, page: int = 1, filters: Optional[Dict[str, Union[str, list]]] = None):
        url = "/products/categories"
        params = {'limit': limit, 'page': page}
        if filters is not None:
            params.update(parse_filters(filters))

        return CategoriesResponse.parse_obj(self._get_request(url, params))

    def create_category(self, name: str, parent_id: Optional[int] = None):
        url = "/products/categories"
        params = {'name': name, parent_id: 'parent_id'}
        Category.parse_obj(self._post_request(url, params))
