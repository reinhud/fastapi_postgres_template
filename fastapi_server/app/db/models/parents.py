"""Sqlalchemy model for 'parent' table.

This is the basic sqlalchemy relationship example 
representing a simple 'ONe-To-Many' relationship pattern.
"""
from sqlalchemy import Column, Date, Numeric, String
from sqlalchemy.orm import relationship

from app.db.models.base import Base, BaseDBModel


class Parent(Base, BaseDBModel):
    """ Database model representing 'parent' table in db.
    
    'id' and 'tablename' are created automatically by 'BaseModel'.
    """

    name = Column(String)
    birthdate = Column(Date)
    height = Column(Numeric)

    children = relationship("Child", back_populates="parent")
