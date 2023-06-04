from pydantic import BaseModel

class BaseEvent(BaseModel):
    event: str
    context: dict

