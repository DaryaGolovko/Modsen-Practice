from pydantic import BaseModel


class Page(BaseModel):
    id: int
    text: str
