"""Sqlalchemy model for 'child' table."""
from sqlalchemy import Column, Date, ForeignKey, Integer, Numeric, String
from sqlalchemy.orm import relationship

from app.db.models.base import Base, BaseDBModel


class Child(Base, BaseDBModel):
    """ Database model representing 'child' table in db.
    
    'id' and 'tablename' are created automatically by 'BaseModel'.
    """

    name = Column(String)
    birthdate = Column(Date)
    height = Column(Numeric)
    hobby= Column(String)
    parent_id = Column(Integer, ForeignKey("parent.id"))
    parent = relationship("Parent", back_populates="children")
