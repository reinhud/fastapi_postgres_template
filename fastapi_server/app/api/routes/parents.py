"""Endpoints for 'parent' ressource."""
from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from loguru import logger

from app.api.dependencies.repository import get_repository
from app.db.repositories.parents import ParentRepository
from ..schemas.parents import ParentCreate, ParentInDB, ParentOptionalSchema
from ..schemas.children import ChildInDB


router = APIRouter()


# Basic Parent Endpoints
# =========================================================================== #
@router.post("/", response_model=ParentInDB, name="parents: create-parent", status_code=status.HTTP_201_CREATED)
async def create_parent(
    parent_new: ParentCreate,
    parent_repo: ParentRepository = Depends(get_repository(ParentRepository)),
) -> ParentInDB:
    parent_created = await parent_repo.create(obj_new=parent_new)

    return parent_created


@router.get("/{id}", response_model=ParentInDB | None, name="parents: read-one-parent")
async def read_parent(
    id: int,
    parent_repo: ParentRepository = Depends(get_repository(ParentRepository)),
) -> ParentInDB | None:
     parent_db = await parent_repo.read_by_id(id=id)
     if not parent_db:
        logger.warning(f"No parent with id = {id}.")
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No parent with id = {id}.")

     return parent_db


@router.patch("/{id}", response_model=ParentInDB, name="parents: update-parent")
async def update_parent(
    id: int,
    parent_update: ParentOptionalSchema,
    parent_repo: ParentRepository = Depends(get_repository(ParentRepository)),
) -> ParentInDB:
    parent_updated = await parent_repo.update(id=id, obj_update=parent_update)
    if not parent_updated:
        logger.warning(f"No parent with id = {id}.")
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Unable to update parent with id = {id}, Parent not found")

    return parent_updated


@router.delete("/{id}", response_model=ParentInDB, name="parents: delete-parent")
async def delete_parent(
    id: int,
    parent_repo: ParentRepository = Depends(get_repository(ParentRepository)),
) -> ParentInDB:
    parent_deleted = await parent_repo.delete(id=id)
    if not parent_deleted:
        logger.warning(f"No parent with id = {id}.")
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Unable to delete parent with id = {id}, Parent not found")

    return parent_deleted


@router.get("/", response_model=List[ParentInDB] | None, name="parents: get all parents")
async def list_parents(
    parent_repo: ParentRepository = Depends(get_repository(ParentRepository)),
) -> List[ParentInDB]:
    parents = await parent_repo.list_all()
    return parents


# Basic relationship pattern endpoint
# =========================================================================== #
@router.get("/get_children", name="parents: get-all-children-for-parent") #response_model=List[ChildInDB]
async def get_parent_children(
    id: int,
    parent_repo: ParentRepository = Depends(get_repository(ParentRepository)),
) -> List[ChildInDB] | None:
    children = await parent_repo.get_parent_children_by_id(id=id)
    if children is None:
        logger.info(f"Parent with id: {id} not found.")
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Parent with id: {id} not found.")
    elif not children:
        logger.info(f"Parent with id: {id} has no children.")
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No children found for parent with with id: {id}.")
    return children
