"""Sqlalchemy model for 'child' table."""
from sqlalchemy import Column, Date, ForeignKey, String, UUID
from sqlalchemy.orm import relationship

from .base import Base


class Child(Base):
    """ Database model representing 'child' table in db.
    
    'id' and 'tablename' are created automatically by 'BaseModel'.
    """

    name = Column(String)
    birthdate = Column(Date)
    hobby= Column(String)
    parent_id = Column(UUID, ForeignKey("parent.id"))
    parent = relationship("Parent", back_populates="children")
