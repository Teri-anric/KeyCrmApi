from typing import List

from pydantic import BaseModel, Field


class Buyer(BaseModel):
    id: int = Field(..., example=22, description="Ідентифікатор покупця")
    full_name: str = Field(..., example="John Doe", nullable=False, description="Повне ім'я покупця")
    email: List[str] = Field(None, example=["john.doe@mail.app", "john.doe2@mail.app"], nullable=True,
                             description="Список електронних адрес покупця")
    phone: List[str] = Field(None, example=["+1 555-234-1234", "+1 555-234-7777"], nullable=True,
                             description="Список телефонів покупця")
    note: str = Field(None, example="Примітка", nullable=True, description="Примітка")
    created_at: str = Field(..., example="2020-05-16 17:00:07", description="Дата створення покупця в UTC форматі")
    updated_at: str = Field(..., example="2020-05-16 17:00:07",
                            description="Дата останньої зміни покупця в UTC форматі")
