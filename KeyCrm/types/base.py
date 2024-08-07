from pydantic import BaseModel, HttpUrl
from typing import List, Optional, Any, TypeVar, Generic, Iterator

ItemType = TypeVar('ItemType')

class ListResponse(BaseModel, Generic[ItemType]):
    """
    Represents a List response.
    """

    total: int
    """
    Number of total items found in the query.
    Example: 100
    """

    current_page: int
    """
    Current page number.
    Example: 1
    """

    per_page: int
    """
    Number of items in the array for each request.
    Example: 15
    """

    data: List[ItemType]
    """
    The actual data array representing the items in the response.
    """

    first_page_url: HttpUrl
    """
    URL for the first page of the response.
    Example: https://openapi.keycrm.app/{current_path}?page=1
    """

    last_page_url: HttpUrl
    """
    URL for the last page of the response.
    Example: https://openapi.keycrm.app/{current_path}?page=5
    """

    next_page_url: Optional[HttpUrl]
    """
    URL for the next page of the response.
    Example: https://openapi.keycrm.app/{current_path}?page=2
    """

    def __iter__(self) -> Iterator[ItemType]:
        return iter(self.data)

    def __getitem__(self, item) -> ItemType:
        return self.data[item]