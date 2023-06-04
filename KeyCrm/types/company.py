from pydantic import BaseModel

class Company(BaseModel):
    """
    Information about the customer's company.
    Returned only when include=company is specified.
    """

    id: int
    """
    ID of the company.
    Example: 1
    """

    name: str
    """
    Name of the company.
    Example: Keycrm
    """

    full_name: Optional[str] = None
    """
    Full name of the company.
    Example: ТОВ Кейцрм
    """

    address: Optional[str] = None
    """
    Address of the company.
    Example: ТОВ Кейцрм
    """

    banking_details: Optional[str] = None
    """
    Banking details of the company.
    Example: UA123456789101112
    """

    note: Optional[str] = None
    """
    Note about the company.
    Example: Примітка
    """

    created_at: Optional[str] = None
    """
    Creation date of the customer in UTC format.
    Example: 2020-05-16 17:00:07
    """

    updated_at: Optional[str] = None
    """
    Last updated date of the customer in UTC format.
    Example: 2020-05-16 17:00:07
    """