from fastapi import APIRouter, HTTPException

from schemas.product import productDetail
from .auth import get_api_key

router = APIRouter()

@router.get("/{product_id}")
async def readProductId(product_id: str, api_key: str = Depends(get_api_key)):
    return {"product_id": product_id}

@router.put("/detail/{product_id}")
async def readProductDetail(product_id: str, model: productDetail, api_key: str = Depends(get_api_key)):
    model_dict = model.dict()
    if model.price == None:
        raise HTTPException(status_code=404, detail="No price!")
    return {"product_id": product_id, **model_dict}