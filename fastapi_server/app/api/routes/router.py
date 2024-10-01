"""Bundling of endpoint routers.

Import and add all endpoint routers here.
"""
from fastapi import APIRouter

from app.api.routes import children, parents


router = APIRouter()

router.include_router(children.router)
router.include_router(parents.router)
