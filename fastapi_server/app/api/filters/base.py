import uuid
from datetime import datetime

from fastapi_filter.contrib.sqlalchemy import Filter as SQLAlchemyFilter

class BaseFilter(SQLAlchemyFilter):
    id: uuid.UUID | None = None
    id__in: list[uuid.UUID] | None = None
    created_at__gte: datetime | None = None
    created_at__lte: datetime | None = None
    updated_at__gte: datetime | None = None
    updated_at__lte: datetime | None = None
    
    # Default sorting by updated_at with most recent first
    order_by: list[str] | None = ['-updated_at']
