import datetime as dt
import uuid
from typing import Optional

from fastapi_filter.contrib.sqlalchemy import Filter

from .base import BaseFilter
from ..schemas.children import ChildInDB


class ChildFilter(BaseFilter):
    name: Optional[str] = None
    birthdate: Optional[dt.date] = None
    birthdate__gte: Optional[dt.date] = None
    birthdate__lte: Optional[dt.date] = None
    hobby: Optional[str] = None
    parent_id: Optional[uuid.UUID] = None

    order_by: list[str] = ["name"]
    search: Optional[str] = None

    class Constants(Filter.Constants):
        model = ChildInDB
        search_model_fields = ["name"]