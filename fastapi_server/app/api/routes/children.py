"""Endpoints for 'children' ressource."""
from typing import List

from fastapi import APIRouter, Depends, status
from fastapi_filter import FilterDepends

from app.api.dependencies.repository import get_repository
from app.db.repositories.children import ChildRepository

from ..filters.children import ChildFilter
from ..schemas.children import ChildCreate, ChildInDB, ChildWithParent, ChildUpdate


router = APIRouter(
    prefix="/children",
    tags=["children"]
)


# Basic Parent Endpoints
# =========================================================================== #
@router.post("/", response_model=ChildInDB, status_code=status.HTTP_201_CREATED)
async def create_child(
    child_new: ChildCreate,
    child_repo: ChildRepository = Depends(get_repository(ChildRepository)),
) -> ChildInDB:
    return await child_repo.create(obj_new=child_new)

@router.get("/{child_id}", response_model=ChildWithParent | None)
async def read_child(
    child_id: int,
    child_repo: ChildRepository = Depends(get_repository(ChildRepository)),
) -> ChildInDB | None:
     return await child_repo.read(id=child_id)

@router.patch("/{child_id}", response_model=ChildInDB)
async def update_child(
    child_id: int,
    child_update: ChildUpdate,
    child_repo: ChildRepository = Depends(get_repository(ChildRepository)),
) -> ChildInDB:
    return await child_repo.update(id=child_id, obj_update=child_update)
    
@router.delete("/{child_id}", response_model=ChildInDB)
async def delete_child(
    child_id: int,
    child_repo: ChildRepository = Depends(get_repository(ChildRepository)),
) -> ChildInDB:
    return await child_repo.delete(id=child_id)

@router.get("/", response_model=List[ChildInDB])
async def list_children(
    child_filter = FilterDepends(ChildFilter),
    child_repo: ChildRepository = Depends(get_repository(ChildRepository)),
) -> List[ChildInDB]:
    return await child_repo.filtered_list(list_filter=child_filter)
