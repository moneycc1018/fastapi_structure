from fastapi import APIRouter

from api.api_v1.endpoints.product import product
from api.api_v1.endpoints.user import user

api_router = APIRouter()
api_router.include_router(user.router, prefix="/user", tags=["user"])
api_router.include_router(product.router, prefix="/product", tags=["product"])