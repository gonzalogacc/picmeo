from datetime import datetime
from typing import List, Optional, Dict, Union
from typing_extensions import Annotated
from pydantic import BaseModel, Field, BeforeValidator


class MissingParametersException(Exception):
    ...


class VerificationException(Exception):
    ...


class Contact(BaseModel):
    wa_id: str
    profile: dict


class Button(BaseModel):
    payload: str
    text: str


class ReferredProduct(BaseModel):
    catalog_id: str
    product_retailer_id: str


class Context(BaseModel):
    forwarded: bool
    frequently_forwarded: Optional[bool]
    from_: str = Field(alias="from")
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
    id: str
    caption: Optional[str] = None
    mime_type: str
    sha256: str


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


class Location(BaseModel):
    latitude: float
    longitude: float
    name: Optional[str] = None
    address: Optional[str] = None


def _epoch_str_parser(t: str):
    return datetime.fromtimestamp(int(t))


EpochDatetime = Annotated[datetime, BeforeValidator(_epoch_str_parser)]


class MessageBase(BaseModel):
    id: str
    timestamp: EpochDatetime
    from_: str = Field(alias="from")
    type: str


class Audio(BaseModel):
    id: str
    mime_type: str


class AudioMessage(MessageBase):
    audio: Audio


class TextMessage(MessageBase):
    # test_ping_message = {'object': 'whatsapp_business_account', 'entry': [{'id': '104246805978102', 'changes': [{'value': {'messaging_product': 'whatsapp', 'metadata': {'display_phone_number': '34623508545', 'phone_number_id': '102033176202052'}, 'contacts': [{'profile': {'name': 'Gonza'}, 'wa_id': '447472138610'}], 'messages': [{'from': '447472138610', 'id': 'wamid.HBgMNDQ3NDcyMTM4NjEwFQIAEhgUM0ExNzRFRTcyRDc3MTAzNjM3RkEA', 'timestamp': '1705880589', 'text': {'body': 'ping'}, 'type': 'text'}]}, 'field': 'messages'}]}]}
    text: Text


class ImageMessage(MessageBase):
    image: Image


class Reaction(BaseModel):
    message_id: str
    emoji: str


class ReactionMessage(MessageBase):
    reaction: Reaction


class StickerMessage(MessageBase):
    sticker: Sticker


class LocationMessage(MessageBase):
    location: Location


class Name(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    formatted_name: str


class Phone(BaseModel):
    phone: str
    wa_id: str
    type: str


class ContactElement(BaseModel):
    name: Name
    phones: List[Phone]


class ContactMessage(MessageBase):
    contacts: List[ContactElement]


class Value(BaseModel):
    messaging_product: str
    metadata: dict
    contacts: List[Contact]
    messages: List[ContactMessage]
    # messages: List[Union[AudioMessage, TextMessage, ImageMessage, ReactionMessage, StickerMessage, LocationMessage, ContactMessage]]
    errors: Optional[str] = None  # Implement
    statuses: Optional[dict] = None


class Change(BaseModel):
    value: Value
    field: str


class Entry(BaseModel):
    id: str
    changes: List[Change]


class WebHookNotification(BaseModel):
    object: str  # whatsapp_business_account
    entry: List[Entry]
