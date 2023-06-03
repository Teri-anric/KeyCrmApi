from typing import List, Union
from urllib.parse import quote

from KeyCrm.UserApi.types.product import Product


class ProductMinix:
    def create_product(self, product: Product):
        url = "catalog/products"
        self.post_request(url, params=product.json())

    def delete_products(self, ids: List[Union[int, str]]):
        if not ids:
            return
        url = "batch/products/execute/remove?filters[id]=" + quote(",".join(map(str, ids)))
        return self._post_request(url).get("result")
