from typing import Generic, TypeVar, Type

from pydantic import BaseModel

from app.db.base_class import Base

ModelType = TypeVar("ModelType", bound=Base)
CreateDtoType = TypeVar("CreateDtoType", bound=BaseModel)


class BaseService(Generic[ModelType, CreateDtoType]):

    def __init__(self, model: Type[ModelType]):
        self.model = model