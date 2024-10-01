"""Pydantic domain models for 'children' ressource."""
import datetime as dt
from typing import Optional

from .base import BaseSchema, IDSchemaMixin
# from .parents import ParentInDB


class ChildBase(BaseSchema):
    name: str
    birthdate: Optional[dt.date]
    hobby: Optional[str]
    parent_id: int

class ChildInDB(ChildBase, IDSchemaMixin):
    """Schema for 'child' in database."""
    pass

class ChildCreate(ChildBase):
    pass

class ChildUpdate(ChildInDB):
    pass

class ChildWithParent(ChildInDB):
    # parent: ParentInDB
    pass
