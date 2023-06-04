from typing import List

from pydantic import BaseModel, HttpUrl
from datetime import datetime


class File(BaseModel):
    """
    Represents a file.
    """

    id: int
    """
    The identifier of the file in the system.
    """

    file_name: str
    """
    The encrypted name of the uploaded file.
    Example: 6XTec5rSOzA5c9yi7LShrJ8sRwsOHvqc.jpeg
    """

    url: HttpUrl
    """
    The URL of the uploaded file.
    Example: https://openapi.keycrm.app/storage/comany-name/6XTec5rSOzA5c9yi7LShrJ8sRwsOHvqc.jpeg
    """

    size: int
    """
    The size of the uploaded file in bytes.
    Example: 563263
    """

    extension: str
    """
    The extension of the file.
    Example: png
    """

    original_file_name: str
    """
    The original name of the uploaded file.
    Example: my-image.png
    """

    mime_type: str
    """
    The MIME type of the uploaded file.
    Example: image/png
    """

    created_at: datetime
    """
    The creation date of the file in UTC format.
    Example: 2020-05-16 16:56:44
    """

    updated_at: datetime
    """
    The last modification date of the file in UTC format.
    Example: 2020-05-16 16:56:44
    """



class ListFile(BaseModel):
    """
    An array of Files in the response from the server
    """

    data: List[File]
    """
    List for Files
    """
