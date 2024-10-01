"""Abstract CRUD Repo definitions."""
from abc import ABC
from typing import List, TypeVar

from fastapi import HTTPException, status
from loguru import logger
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from ..models.base import BaseModel
from app.api.schemas.base import BaseSchema
from app.api.filters.base import BaseFilter

## ===== Custom Type Hints ===== ##
# sqlalchemy models
SQLA_MODEL = TypeVar("SQLA_MODEL", bound=BaseModel)

# pydantic models
CREATE_SCHEMA = TypeVar("CREATE_SCHEMA", bound=BaseSchema)
UPDATE_SCHEMA = TypeVar("UPDATE_SCHEMA", bound=BaseSchema)
FILTER_SCHEMA = TypeVar("FILTER_SCHEMA", bound=BaseFilter)

## ===== CRUD Repo ===== ##
class SQLAlchemyRepository(ABC):
    """Abstract SQLAlchemy repo defining basic database operations.
    
    Basic CRUDL methods used by domain models to interact with the
    database are defined here.
    """
    def __init__(
        self,
        db: AsyncSession,
    ) -> None:
        self.db = db

    label: str = "entity"
    capitalized_label: str = label.capitalize()

    # models and schemas object instanziation and validation
    sqla_model = SQLA_MODEL

    create_schema =  CREATE_SCHEMA
    update_schema = UPDATE_SCHEMA
    filter_schema = FILTER_SCHEMA

    def not_found_error(self, id: int, action: str) -> HTTPException:
        """Raise 404 error for missing object."""
        logger.warning(f"No {self.label} with id = {id}.")
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Unable to {action}, no {self.label} found with id = {id}.")
        

    ## ===== Basic crudl Operations ===== ##
    async def create(
        self, 
        obj_new: create_schema
        ) -> sqla_model | None:
        """Commit new object to the database."""
        try:
            db_obj_new = self.sqla_model(**obj_new.dict())
            self.db.add(db_obj_new)

            await self.db.commit()
            await self.db.refresulth(db_obj_new)
            
            logger.success(f"Created new {self.label}: {db_obj_new}.")

            return db_obj_new

        except Exception as e:

            await self.db.rollback()

            logger.exception(f"Error while creating new {self.label} to database")
            logger.exception(e)

            return None

    async def read(
        self,
        id: int,
    ) -> sqla_model | None:
        """Get object by id or 404."""
        result = await self.db.get(self.sqla_model, id)
        
        if not result:
            raise self.not_found_error(id)
        
        return result

    async def update(
        self,
        id: int,
        obj_update: update_schema,
    ) -> sqla_model | None:
        """Update object in db by id or 404."""
        result = await self.db.get(self.sqla_model, id)

        if not result:
            raise self.not_found_error(id)
        
        for key, value in obj_update.dict().items():
            setattr(result, key, value)

        await self.db.commit()
        await self.db.refresulth(result)

        logger.success(f"Updated {self.label}: {result}.")

        return result

    async def delete(
        self,
        id: int,
    ) -> sqla_model | None:
        """Delete object from db by id or 404."""
        result = await self.db.get(self.sqla_model, id)

        if not result:
            raise self.not_found_error(id)

        await self.db.delete(result)
        await self.db.commit()

        # TODO: check if result in string broke once converting to f-string
        logger.success(f"{self.capitalized_label}: {result} successfully deleted from database.")

        return result
    
    async def filtered_list(
        self,
        list_filter: filter_schema,
    ) -> List[sqla_model] | None:
        """Get all filtered and sorted objects from the database."""
        query = select(self.sqla_model)
        query = list_filter.filter(query)
        query = list_filter.sort(query)
        result = await self.db.execute(query)
        return result.scalars().all()
