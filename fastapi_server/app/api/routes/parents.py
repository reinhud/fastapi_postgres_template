"""Endpoints for 'parent' ressource."""
from typing import List

from fastapi import APIRouter, Depends, status
from fastapi_filter import FilterDepends

from app.api.dependencies.repository import get_repository
from app.db.repositories.parents import ParentRepository

from ..schemas.parents import ParentCreate, ParentInDB, ParentUpdate, ParentWithChildren
# from ..schemas.children import ChildInDB
from ..filters.parents import ParentFilter


router = APIRouter(
    prefix="/parents",
    tags=["parents"]
)


# Basic Parent Endpoints
# =========================================================================== #
@router.post("/", response_model=ParentInDB, status_code=status.HTTP_201_CREATED)
async def create_parent(
    parent_new: ParentCreate,
    parent_repo: ParentRepository = Depends(get_repository(ParentRepository)),
) -> ParentInDB:
    return await parent_repo.create(obj_new=parent_new)


@router.get("/{parent_id}", response_model=ParentWithChildren)
async def read_parent(
    parent_id: int,
    parent_repo: ParentRepository = Depends(get_repository(ParentRepository)),
) -> ParentWithChildren:
    return await parent_repo.read(id=parent_id)


@router.patch("/{parent_id}", response_model=ParentInDB)
async def update_parent(
    parent_id: int,
    parent_update: ParentUpdate,
    parent_repo: ParentRepository = Depends(get_repository(ParentRepository)),
) -> ParentInDB:
    return await parent_repo.update(id=parent_id, obj_update=parent_update)


@router.delete("/{parent_id}", response_model=ParentInDB)
async def delete_parent(
    parent_id: int,
    parent_repo: ParentRepository = Depends(get_repository(ParentRepository)),
) -> ParentInDB:
    return await parent_repo.delete(id=parent_id)


@router.get("/", response_model=List[ParentInDB])
async def list_parents(
    parent_filter = FilterDepends(ParentFilter),
    parent_repo: ParentRepository = Depends(get_repository(ParentRepository)),
) -> List[ParentInDB]:
    return await parent_repo.filtered_list(parent_filter)


# # Basic relationship pattern endpoint
# # =========================================================================== #
# @router.get("/get_children", name="parents: get-all-children-for-parent") #response_model=List[ChildInDB]
# async def get_parent_children(
#     id: int,
#     parent_repo: ParentRepository = Depends(get_repository(ParentRepository)),
# ) -> List[ChildInDB] | None:
#     children = await parent_repo.get_children_by_parent_id(id=id)
#     if children is None:
#         logger.info(f"Parent with id: {id} not found.")
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Parent with id: {id} not found.")
#     elif not children:
#         logger.info(f"Parent with id: {id} has no children.")
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No children found for parent with with id: {id}.")
#     return children
