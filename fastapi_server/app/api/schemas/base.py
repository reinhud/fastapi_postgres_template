"""Base classes for pydantic domain models.

Allows for pydantic validation via inheritence from pydantics 'BaseModel'
"""
import datetime as dt
import uuid
from pydantic import BaseModel

class BaseSchema(BaseModel):
    """Base pydantic schema for domain models.
    
    Share common logic here.
    """
    pass

class IDSchemaMixin(BaseModel):
    """Base pydantic schema to be inherited from by database schemata."""
    id: uuid.UUID
    created_at: dt.datetime
    updated_at: dt.datetime

    class Config:
        from_attributes = True
