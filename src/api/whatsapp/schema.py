from datetime import datetime
from typing import List, Optional, Dict

from pydantic import BaseModel, Field


class Contact(BaseModel):
    wa_id: str
    profile: dict


class AudioMessage(BaseModel):
    id: str
    mime_type: str


class Button(BaseModel):
    payload: str
    text: str


class ReferredProduct(BaseModel):
    catalog_id: str
    product_retailer_id: str


class Context(BaseModel):
    forwarded: bool
    frequently_forwarded: Optional[bool]
    _from: str = Field(alias="from")
    id: str
    referred_product: Optional[ReferredProduct]


class Document(BaseModel):
    caption: str
    filename: str
    sha256: str
    mime_type: str
    id: str


class Error(BaseModel):
    code: str
    title: str
    message: str
    error_data: dict


class Identity(BaseModel):
    acknowledged: str
    created_timestamp: str
    hash: str


class Image(BaseModel):
    caption: str
    sha256: str
    id: str
    mime_type: str


class Interactive(BaseModel):
    type: dict


class ProductItem(BaseModel):
    product_retailer_id: str
    quantity: str
    item_price: str
    currency: str


class Order(BaseModel):
    catalog_id: str
    text: str
    product_items: List[ProductItem]


class Sticker(BaseModel):
    mime_type: str
    sha256: str
    id: str
    animated: Optional[bool]


class Text(BaseModel):
    body: str


class Video(BaseModel):
    caption: str
    filename: str
    sha256: str
    id: str
    mime_type: str


class Reaction(BaseModel):
    message_id: str
    emoji: str


class Location(BaseModel):
    latitude: float
    longitude: float
    name: str
    address: str


class MessageBase(BaseModel):
    id: str
    timestamp: datetime
    from_: str = Field(alias="from")
    type: str


class TextMessage(MessageBase):
    text: Text


class ImageMessage(MessageBase):
    image: Image


class Audio(MessageBase):
    id: str
    mime_type: str


class AudioMessage(MessageBase):
    audio: Audio


class ReactionMessage(MessageBase):
    reaction: Reaction


class StickerMessage(MessageBase):
    sticker: Sticker


class LocationMessage(MessageBase):
    location: Location


class ContactMessage(MessageBase):
    contacts: List[Contact]


class Value(BaseModel):
    contacts: List[Contact]
    errors: Optional[Dict]  # Implement
    messaging_product: str
    messages: List[TextMessage | ImageMessage | ReactionMessage | StickerMessage | LocationMessage | ContactMessage | AudioMessage]
    metadata: dict
    statuses: Optional[dict]


class Change(BaseModel):
    value: Value
    field: str


class Entry(BaseModel):
    id: str
    changes: List[Change]


class WebHookNotification(BaseModel):
    object: str  # whatsapp_business_account
    entry: List[Entry]
