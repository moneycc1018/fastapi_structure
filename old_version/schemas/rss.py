from pydantic import BaseModel


class RssInfoResponse(BaseModel):
    source_id: str
    source_name: str
    price: int
    rss_url: str
    source_url: str
    logo_url: str

    class Config:
        orm_mode = True
