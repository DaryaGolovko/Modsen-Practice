from pydantic import BaseModel


class Page(BaseModel):
    id: int
    text: str
    date_creation: str = None
    rubrics: str
    class Config:
        orm_mode = True
