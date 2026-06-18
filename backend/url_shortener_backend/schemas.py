from pydantic import BaseModel, HttpUrl

class URLCreate(BaseModel):
    url: HttpUrl

class URLRead(BaseModel):
    code: str
    original_url: str
    short_url: str