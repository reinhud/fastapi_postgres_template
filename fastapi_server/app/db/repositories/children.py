"""Domain Repository for 'child' entity.

All logic related to the child entity is defined and grouped here.
"""
from app.db.models.children import Child as ChildModel
from app.db.repositories.base import SQLAlchemyRepository
from app.api.schemas.children import ChildCreate, ChildUpdate
from app.api.filters.children import ChildFilter


class ChildRepository(SQLAlchemyRepository):
    """Handle all logic related to Child entity.
    
    Inheritence from 'SQLAlchemyRepository' allows for 
    crudl functionality, only schemata and models used have to be defined.
    """
    label = "child"
    
    sqla_model = ChildModel

    create_schema = ChildCreate
    update_schema = ChildUpdate
    filter_schema = ChildFilter
