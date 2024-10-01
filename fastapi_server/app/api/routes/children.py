"""Endpoints for 'children' ressource."""
from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from loguru import logger

from app.api.dependencies.repository import get_repository
from app.db.repositories.children import ChildRepository

from ..filters.children import ChildFilter
from ..schemas.children import ChildCreate, ChildInDB, ChildWithParent, ChildUpdate


router = APIRouter()


# Basic Parent Endpoints
# =========================================================================== #
@router.post("/post", response_model=ChildInDB, name="Children: create-child", status_code=status.HTTP_201_CREATED)
async def create_child(
    child_new: ChildCreate,
    child_repo: ChildRepository = Depends(get_repository(ChildRepository)),
) -> ChildInDB:
    child_created = await child_repo.create(obj_new=child_new)

    return child_created

@router.get("/{id}", response_model=ChildWithParent | None, name="children: read-one-child")
async def read_child(
    id: int,
    child_repo: ChildRepository = Depends(get_repository(ChildRepository)),
) -> ChildInDB | None:
     child_db = await child_repo.read_by_id(id=id)
     if not child_db:
        logger.warning(f"No child with id = {id}.")
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No child with id = {id}.")

     return child_db

@router.patch("/update", response_model=ChildInDB, name="children: update-child")
async def update_child(
    id: int,
    child_update: ChildUpdate,
    child_repo: ChildRepository = Depends(get_repository(ChildRepository)),
) -> ChildInDB:
    child_updated = await child_repo.update(id=id, obj_update=child_update)
    if not child_updated:
        logger.warning(f"No child with id = {id}.")
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Unable to update child with id = {id}, Child not found")

    return child_updated

@router.delete("/delete", response_model=ChildInDB, name="children: delete-child")
async def delete_child(
    id: int,
    child_repo: ChildRepository = Depends(get_repository(ChildRepository)),
) -> ChildInDB:
    child_deleted = await child_repo.delete(id=id)
    if not child_deleted:
        logger.warning(f"No parent with id = {id}.")
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Unable to delete child with id = {id}, Parent not found")

    return child_deleted

@router.get("/", response_model=List[ChildInDB], name="children: read-all-children")
async def read_all_children(
    child_repo: ChildRepository = Depends(get_repository(ChildRepository)),
    child_filter: ChildFilter = Depends(ChildFilter),
) -> List[ChildInDB]:
    # TODO: would it be better to just return the await?
    children = await child_repo.list(list_filter=child_filter)
    return children
