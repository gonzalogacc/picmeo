from uuid import UUID

from pydantic import BaseModel


class User(BaseModel):
    id: UUID
    phone_number: str
    name: str


class Image(BaseModel):
    id: UUID
    image_url: str
    image_md5: str
