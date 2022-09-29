from pydantic import BaseModel, Field
from typing import Optional, List

class productImage(BaseModel):
    name: str
    url: str

class productDetail(BaseModel):
    name: str
    brand: str
    price: float = None
    description: Optional[str] = Field(default=None, max_length=100)
    images: Optional[List[productImage]] = None
    is_sold: bool = False