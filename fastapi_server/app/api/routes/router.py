"""Bundling of endpoint routers.

Import and add all endpoint routers here.
"""
from fastapi import APIRouter

from app.api.routes import children, parents


router = APIRouter()

# TODO: look into tags here
router.include_router(children.router, prefix="/children")
router.include_router(parents.router, prefix="/parents")
