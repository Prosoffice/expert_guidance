from typing import Optional

from pydantic import BaseModel


class GuidanceBase(BaseModel):
    query: Optional[str] = None
    user_id: Optional[int] = None
    result: Optional[str] = None
    content: Optional[str] = None
    context: Optional[int] = None


class GuidanceCreateDto(GuidanceBase):
    query: str


class GuidanceBaseInDbBase(GuidanceBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True


class Guidance(GuidanceBaseInDbBase):
    pass

