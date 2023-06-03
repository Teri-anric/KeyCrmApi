class FieldProducts:
    @staticmethod
    def get(item):
        return f"products.{item}"

    def __getattr__(self, item):
        self.get(item)

    primary_key = 'products.primary_key'
    name = 'products.name'
    description = 'products.description'
    currency_code = 'products.currency_code'
    category_name = 'products.category_name'
    thumbnail = 'products.thumbnail'
    weight = 'products.weight'
    length = 'products.length'
    height = 'products.height'
    width = 'products.width'


class FieldOffers:
    @staticmethod
    def get(item):
        return f"products.{item}"

    def __getattr__(self, item):
        self.get(item)

    id = 'offers.id'
    sku = 'offers.sku'
    barcode = 'offers.barcode'
    price = 'offers.price'
    purchased_price = 'offers.purchased_price'
    weight = 'offers.weight'
    length = 'offers.length'
    height = 'offers.height'
    width = 'offers.width'
    property_name = 'offers.property_name'
    property_value = 'offers.property_value'
