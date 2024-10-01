"""Pydantic domain models for 'parents' ressource."""
import datetime as dt
from typing import Optional

from .base import BaseSchema, IDSchemaMixin
from .children import ChildInDB


class ParentBase(BaseSchema):
    name: str
    birthdate: Optional[dt.date]

class ParentInDB(ParentBase, IDSchemaMixin):
    """Schema for 'parent' in database."""
    pass

class ParentCreate(ParentBase):
    pass

class ParentUpdate(ParentInDB):
    pass

class ParentWithChildren(ParentInDB):
    # children_ids: list[int] = []
    # children: list[ChildInDB] = []
    pass
