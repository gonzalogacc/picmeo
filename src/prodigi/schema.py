from datetime import datetime
from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class ProductDimensions(BaseModel):
    width: float
    height: float
    units: str  ## Enum perhaps?


class WrapEnum(str, Enum):
    black = "Black"
    image_wrap = "ImageWrap"
    mirror_wrap = "MirrorWrap"
    white = "White"


class ProductAttributes(BaseModel):
    wrap: List[WrapEnum]


class Required(BaseModel):
    required: bool


class ProductPrintAreas(BaseModel):
    default: Required


class VariantAttributes(BaseModel):
    wrap: str


class ProductVariant(BaseModel):
    attributes: VariantAttributes
    # shipsTo: List[ShipsToEnum]
    # printAreaSizes: VariantPrintAreaSizes


class ProductVariants(BaseModel):
    variants: List[ProductVariant]


class ProductDetails(BaseModel):
    sku: str
    description: str
    productDimensions: ProductDimensions
    attributes: ProductAttributes
    printAreas: ProductPrintAreas
    variants: ProductVariants


class PrintAreaDimensions(BaseModel):
    horizontalResolution: int
    VerticalResolution: int


class VariantPrintAreaSizes(BaseModel):
    default: PrintAreaDimensions


class StatusDetailsStatusEnum(str, Enum):
    not_started = 'NotStarted'
    in_progress = 'InProgress'
    complete = 'Complete'
    error = 'Error'


class OrderStatusDetails(BaseModel):
    downloadAssets: StatusDetailsStatusEnum
    printReadyAssetsPrepared: StatusDetailsStatusEnum
    allocateProductionLocation: StatusDetailsStatusEnum
    inProduction: StatusDetailsStatusEnum
    shipping: StatusDetailsStatusEnum


class StatusEnum(str, Enum):
    in_progress = 'InProgress'
    complete = 'Complete'
    cancelled = 'Cancelled'


class OrderIssue(BaseModel):
    objectId: str
    errorCode: str
    description: str
    authorisationDetails: str


class OrderStatus(BaseModel):
    stage: StatusEnum
    issues: List[str]
    details: OrderStatusDetails


class MoneyAmount(BaseModel):
    amount: str
    currency: str


class OrderCostItem(BaseModel):
    id: str
    itemId: Optional[str]
    cost: MoneyAmount
    shipmentId: Optional[str] = None
    chargeType: str


class OrderCharge(BaseModel):
    id: str
    prodigiInvoiceNumber: Optional[str]
    totalCost: MoneyAmount
    totalTax: MoneyAmount
    items: List[OrderCostItem]


class OrderCarrier(BaseModel):
    name: str
    service: str


class OrderFulfillmentLocation(BaseModel):
    countryCode: str
    labCode: str


class OrderTracking(BaseModel):
    number: str
    url: str


class OrderShipment(BaseModel):
    id: str
    dispatchDate: datetime
    carrier: OrderCarrier
    fulfillmentLocation: OrderFulfillmentLocation
    tracking: OrderTracking
    items: List[dict]
    status: str


class Address(BaseModel):
    line1: str
    line2: str
    postalOrZipCode: str
    countryCode: str
    townOrCity: str
    stateOrCounty: Optional[str] = None


class Recipient(BaseModel):
    name: str
    email: Optional[str] = None
    phoneNumber: Optional[str] = None
    address: Address


class ItemAsset(BaseModel):
    id: str
    printArea: str
    md5Hash: str
    url: str
    thumbnailUrl: str
    status: str


class ItemStatusEnum(str, Enum):
    ok = 'Ok'


class SizingEnum(str, Enum):
    fill_print_area = 'fillPrintArea'
    fit_print_area = 'fitPrintArea'
    stretch_to_print_area = 'stretchToPrintArea'


class Item(BaseModel):
    id: str
    status: ItemStatusEnum
    merchantReference: str
    sku: str
    copies: int
    sizing: SizingEnum
    thumbnailUrl: str
    attributes: dict
    assets: List[ItemAsset]
    recipientCost: MoneyAmount
    correlationIdentifier: str


class OrderMetadata(BaseModel):
    mycustomkey: str
    someCustomerPreference: dict


class Callback(BaseModel):
    ## TODO: Calbback schema still not implemented
    pass


class ShippingMethodEnum(str, Enum):
    budget = 'Budget'
    standard = 'Standard'
    express = 'Express'
    overnight = 'Overnight'


class PackingSlip(BaseModel):
    url: str
    status: str


class OrderResponse(BaseModel):
    id: str
    created: datetime
    lastUpdated: datetime
    callbackUrl: Optional[Callback] = None
    merchantReference: Optional[str] = None
    shippingMethod: ShippingMethodEnum
    idempotencyKey: Optional[str] = None
    status: OrderStatus
    charges: List[OrderCharge]
    shipments: List[OrderShipment]
    recipient: Recipient
    items: List[Item]
    packingSlip: Optional[PackingSlip] = None
    metadata: OrderMetadata


class OutcomeEnum(str, Enum):
    ok = "Ok"


class RequestResponse(BaseModel):
    outcome: OutcomeEnum
    order: OrderResponse
    traceParent: str


class OrderIN(BaseModel):
    pass
