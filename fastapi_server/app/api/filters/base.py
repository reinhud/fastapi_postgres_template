import uuid
from datetime import datetime

from fastapi_filter.contrib.sqlalchemy import Filter as SQLAlchemyFilter

class BaseFilter(SQLAlchemyFilter):
    id: uuid.UUID | None
    id__in: list[uuid.UUID] | None
    created_at: datetime | None
    created_at__gt: datetime | None
    created_at__lt: datetime | None
    created_at__gte: datetime | None
    created_at__lte: datetime | None
    updated_at: datetime | None
    updated_at__gt: datetime | None
    updated_at__lt: datetime | None
    updated_at__gte: datetime | None
    updated_at__lte: datetime | None
    