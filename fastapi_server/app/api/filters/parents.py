import datetime as dt
from typing import Optional

from fastapi_filter.contrib.sqlalchemy import Filter

from app.db.models.parents import Parent

from .base import BaseFilter



class ParentFilter(BaseFilter):
    name: Optional[str] = None
    birthdate: Optional[dt.date] = None
    birthdate__gte: Optional[dt.date] = None
    birthdate__lte: Optional[dt.date] = None

    order_by: list[str] = ["name"]
    search: Optional[str] = None

    class Constants(Filter.Constants):
        model = Parent
        search_model_fields = ["name"]
