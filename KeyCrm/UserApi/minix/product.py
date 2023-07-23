from typing import List, Union
from urllib.parse import quote

from KeyCrm.UserApi.types.product import Product
import json

class ProductMinix:
    def create_product(self, product: Product):
        url = "catalog/products"
        return Product.parse_obj(self._post_request(url, data=json.dumps(product.dict())))

    def delete_products(self, ids: List[Union[int, str]]):
        if not ids:
            return
        url = "batch/products/execute/remove?filters[id]=" + quote(",".join(map(str, ids)))
        return self._post_request(url).get("result")
