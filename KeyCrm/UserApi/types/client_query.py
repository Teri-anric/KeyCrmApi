from typing import List, Optional, Any
from pydantic import BaseModel

class Profile(BaseModel):
    """
    Represents a profile.
    """

    id: int
    """
    The ID of the profile.
    """

    client_id: int
    """
    The ID of the client.
    """

    field: str
    """
    The field of the profile.
    """

    value: str
    """
    The value of the profile.
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

class Client(BaseModel):
    """
    Represents a client.
    """

    id: int
    """
    The ID of the client.
    """

    company_id: Optional[int]
    """
    The ID of the company.
    """

    full_name: str
    """
    The full name of the client.
    """

    phone: Optional[str]
    """
    The phone number of the client.
    """

    email: Optional[str]
    """
    The email address of the client.
    """

    note: Optional[str]
    """
    The note about the client.
    """

    picture: Optional[str]
    """
    The picture of the client.
    """

    image: Optional[str]
    """
    The image of the client.
    """

    orders_sum: str
    """
    The sum of orders for the client.
    """

    currency: str
    """
    The currency of the orders.
    """

    orders_count: int
    """
    The count of orders for the client.
    """

    has_duplicates: int
    """
    Indicates if the client has duplicates.
    """

    manager_id: Optional[int]
    """
    The ID of the manager associated with the client.
    """

    deleted_at: Optional[str]
    """
    The deletion timestamp of the client.
    """

    created_at: str
    """
    The creation timestamp of the client.
    """

    updated_at: str
    """
    The last modification timestamp of the client.
    """

    last_order_created_at: Optional[str]
    """
    The creation timestamp of the last order for the client.
    """

    profiles: List[Profile]
    """
    The profiles associated with the client.
    """

    shipping_addresses: List[str]
    """
    The shipping addresses of the client.
    """

    company: Optional[Company]
    """
    The company associated with the client.
    """

class ClientQueryList(BaseModel):
    """
    Represents a list of clients.
    """

    current_page: int
    """
    The current page number.
    """

    data: List[Client]
    """
    The list of clients.
    """

    first_page_url: str
    """
    The URL of the first page.
    """

    last_page: int
    """
    The last page number.
    """

    last_page_url: str
    """
    The URL of the last page.
    """

    next_page_url: Optional[str]
    """
    The URL of the next page.
    """

    path: str
    """
    The URL path.
    """

    per_page: int
    """
    The number of clients per page.
    """

    prev_page_url: Optional[str]
    """
    The URL of the previous page.
    """

    to: int
    """
    The ending index of the clients.
    """

    total: int
    """
    The total number of clients.
    """
