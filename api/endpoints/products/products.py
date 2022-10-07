from fastapi import APIRouter, HTTPException

from models.products import productDetail

router = APIRouter()

@router.get("/{product_id}")
async def readProductId(product_id: str):
    return {"product_id": product_id}

@router.put("/detail/{product_id}")
async def readProductDetail(product_id: str, model: productDetail):
    model_dict = model.dict()
    if model.price == None:
        raise HTTPException(status_code=404, detail="No price!")
    return {"product_id": product_id, **model_dict}