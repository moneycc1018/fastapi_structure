from fastapi import APIRouter

from api.endpoints.products import products
from api.endpoints.users import users

api_router = APIRouter()
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(products.router, prefix="/products", tags=["products"])