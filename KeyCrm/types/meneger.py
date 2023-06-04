from pydantic import BaseModel
from typing import Optional

class Manager(BaseModel):
    """
    Represents manager information.
    """

    id: int
    """
    Identifier of the manager.
    Example: 1
    """

    first_name: str
    """
    First name of the manager.
    Nullable: false
    Example: John
    """

    last_name: Optional[str] = None
    """
    Last name of the manager.
    Nullable: true
    Example: Doe
    """

    full_name: Optional[str] = None
    """
    Full name of the manager.
    Nullable: true
    Example: John Doe
    """

    username: Optional[str] = None
    """
    Login username of the manager.
    Nullable: true
    Example: johndoe
    """

    email: Optional[str] = None
    """
    Email address of the manager.
    Nullable: true
    Example: john.doe@mail.app
    """

    phone: Optional[str] = None
    """
    Phone number of the manager.
    Nullable: true
    Example: +1 555-234-1234
    """

    role_id: Optional[int] = None
    """
    Identifier of the manager's role.
    Nullable: true
    Example: 2
    """

    status: str
    """
    Status of the manager.
    Nullable: false
    Example: active
    """

    created_at: str
    """
    Creation date of the manager in UTC format.
    Example: 2020-05-16 17:00:07
    """

    updated_at: str
    """
    Last updated date of the manager in UTC format.
    Example: 2020-05-16 17:00:07
    """

    last_logged_at: Optional[str] = None
    """
    Last logged-in date of the manager in UTC format.
    Example: 2020-05-16 17:00:07
    """
