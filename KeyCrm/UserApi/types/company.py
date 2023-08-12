from typing import List, Optional, Any, Iterator
from pydantic import BaseModel

class Field(BaseModel):
    """
    Represents a custom field.
    """

    id: int
    """
    The ID of the field.
    """

    name: str
    """
    The name of the field.
    """

    uuid: str
    """
    The UUID of the field.
    """

    type: str
    """
    The type of the field.
    """

class CustomFieldValue(BaseModel):
    """
    Represents a custom field value.
    """

    id: int
    """
    The ID of the custom field value.
    """

    field_id: int
    """
    The ID of the custom field.
    """

    value: Any
    """
    The value of the custom field.
    """

    field: Field
    """
    The custom field associated with the value.
    """

class Company(BaseModel):
    """
    Represents a company.
    """

    id: int
    """
    The ID of the company.
    """

    name: str
    """
    The name of the company.
    """

    title: Optional[str]
    """
    The title of the company.
    """

    address: Optional[str]
    """
    The address of the company.
    """

    account: Optional[str]
    """
    The account of the company.
    """

    notes: Optional[str]
    """
    The notes of the company.
    """

    created_at: str
    """
    The creation timestamp of the company.
    """

    updated_at: str
    """
    The last modification timestamp of the company.
    """

    custom_field_values: List[CustomFieldValue]
    """
    The custom field values associated with the company.
    """

class CompanyList(BaseModel):
    current_page: int
    data: List[Company]
    first_page_url: str
    from_: int  # Use "from_" to avoid the "from" keyword conflict
    last_page: int
    last_page_url: str
    next_page_url: Optional[str]
    path: str
    per_page: int
    prev_page_url: Optional[str]
    to: int
    total: int

    def __init__(self, **kwargs):
        kwargs['from_'] = kwargs.pop('from')
        super().__init__(**kwargs)

    def __getitem__(self, item: int) -> Company:
        return self.data[item]

    def __iter__(self) -> Iterator[Company]:
        return iter(self.data)