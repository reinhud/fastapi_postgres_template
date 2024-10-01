"""Declaring base model classes for sqlalchemy models."""
import datetime as dt
import uuid

from sqlalchemy import Column, UUID, TIMESTAMP
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.orm import declarative_base


class BaseModel:  
    """Class defining common db model components."""
    id = Column(UUID, primary_key=True, index=True, default=uuid.uuid4)
    created_at = Column(TIMESTAMP(timezone=True), default=dt.datetime.now())
    updated_at = Column(TIMESTAMP(timezone=True), default=dt.datetime.now(), onupdate=dt.datetime.now())

    __name__: str

    # if not declared generate tablename automatically baased on class name 
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()
    
    # refresh server defaults with asyncio 
    # https://docs.sqlalchemy.org/en/14/orm/extensions/asyncio.html#synopsis-orm
    # required in order to access columns with server defaults
    # or SQL expression defaults, subsequent to a flush, without
    # triggering an expired load
    __mapper_args__ = {"eager_defaults": True}

Base = declarative_base(cls=BaseModel)

