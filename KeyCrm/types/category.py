from pydantic import BaseModel
from typing import Optional, List

from .base import ListResponse

class Category(BaseModel):
    """
    Represents a category.
    """

    id: int
    """
    The identifier of the category.
    Example: 1
    """

    name: str
    """
    The name of the category.
    Example: Взуття
    """

    parent_id: Optional[int]
    """
    The identifier of the parent category. For root categories, it will be null.
    Example: 1
    """


class ListCategories(ListResponse):
    """
    An array of Category in the response from the server
    """
    data: List[Category]
