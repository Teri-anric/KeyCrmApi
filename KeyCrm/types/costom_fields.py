from typing import List, Optional
from pydantic import BaseModel


class Option(BaseModel):
    """
    Represents an option for select fields.
    """

    id: int
    """
    The ID of the option.
    """

    field_id: int
    """
    The ID of the field to which the option belongs.
    """

    value: str
    """
    The name of the option.
    """

class CustomField(BaseModel):
    """
    Represents a custom field.
    """

    id: int
    """
    The ID of the field in the system.
    """

    name: str
    """
    The name of the field.
    Example: Варіанти дизайну
    """

    uuid: str
    """
    The external identifier of the field.
    Example: OR_1037
    """

    model: str
    """
    The entity to which the field belongs.
    Possible values: order, lead, client, crm_product
    Example: order
    """

    type: str
    """
    The type of the field.
    Possible values: link, select, switcher, float, number, textarea, text, date, datetime
    Example: select
    """

    required: bool
    """
    Indicates if the field is required.
    Example: true
    """

    position: int
    """
    The position of the field.
    Example: 3
    """

    is_multiple: bool
    """
    Indicates if the field is a multiple select field.
    Example: true
    """

    options: List[Option]
    """
    The options for select fields. For other field types, this list will be empty.
    """
