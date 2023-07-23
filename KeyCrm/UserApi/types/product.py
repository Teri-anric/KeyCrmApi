from typing import List, Optional

from pydantic import BaseModel


class OfferProperty(BaseModel):
    name: str
    value: str


class Offer(BaseModel):
    sku: Optional[str]
    price: Optional[str]
    quantity: Optional[int]
    currency_code: Optional[str]
    weight: Optional[str]
    length: Optional[str]
    height: Optional[str]
    width: Optional[str]
    properties: List[OfferProperty]
    purchased_price: Optional[str]


class CustomFieldValue(BaseModel):
    value: str
    field: dict
    field_id: int


class Product(BaseModel):
    """
    generate for chat-gtp3
    Представляє продукт з різними атрибутами.

    Attributes:
        id (Optional[int]): Унікальний ідентифікатор продукту (якщо доступний).
        name (str): Назва продукту.
        description (str): Опис продукту.
        thumbnail_url (Optional[str]): URL зображення мініатюри продукту (якщо доступний).
        currency_code (str): Код валюти, використаний для цін (наприклад, 'USD', 'EUR' і т.д.).
        weight (str): Вага продукту (наприклад, '1,5 кг', '3 фунти' і т.д.).
        length (str): Довжина продукту (наприклад, '20 см', '8 дюймів' і т.д.).
        height (str): Висота продукту (наприклад, '10 см', '4 дюйми' і т.д.).
        width (str): Ширина продукту (наприклад, '5 см', '2 дюйми' і т.д.).
        has_offers (bool): Прапорець, який позначає, чи є доступні пропозиції для продукту.
        offers (List[Offer]): Список об'єктів Offer, що представляють доступні пропозиції для продукту.
        sku (Optional[str]): Артикул продукту (якщо доступний).
        barcode (Optional[str]): Штрих-код, пов'язаний з продуктом (якщо доступний).
        price (str): Ціна продукту у зазначеній валюті.
        purchased_price (str): Ціна, за яку був придбаний продукт (якщо доступний).
        publications (List[dict]): Список деталей публікацій, пов'язаних з продуктом.
        properties_agg (dict): Словник, що містить агреговані властивості продукту.
        category_id (Optional[int]): Унікальний ідентифікатор категорії, до якої належить продукт (якщо доступний).
        custom_field_values (List[CustomFieldValue]): Список значень користувацьких полів, пов'язаних з продуктом.

    Примітка:
        Клас Product призначений для зберігання інформації про конкретний продукт,
        включаючи його атрибути, ціноутворення, пропозиції та пов'язані деталі.
        Деякі атрибути можуть бути необов'язковими (позначені як Optional),
        що означає, що вони можуть відсутні у деяких продуктів.
        Атрибут offers містить список об'єктів Offer, які представляють різні пропозиції для продукту.
        Атрибут publications містить список деталей публікацій, пов'язаних з продуктом.
        Атрибут custom_field_values містить список значень користувацьких полів, специфічних для продукту.

    """

    id: Optional[int]
    name: str
    description: str
    thumbnail_url: Optional[str]
    currency_code: str
    weight: Optional[str]
    length: Optional[str]
    height: Optional[str]
    width: Optional[str]
    has_offers: Optional[bool]
    offers: Optional[List[Offer]]
    sku: Optional[str]
    barcode: Optional[str]
    price: Optional[str]
    purchased_price: Optional[str]
    publications: Optional[List[dict]]
    properties_agg: Optional[dict]
    category_id: Optional[int]
    custom_field_values: Optional[List[CustomFieldValue]]
    unit_type: Optional[str]
