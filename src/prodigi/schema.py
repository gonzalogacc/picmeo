from datetime import datetime
from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class OutcomeEnum(str, Enum):
    ok = 'Ok'
    created = 'Created'
    validation_failed = 'ValidationFailed'
    cancelled = "Cancelled"
    action_not_available = 'ActionNotAvailable'


class ResponseCommon(BaseModel):
    outcome: OutcomeEnum
    traceParent: str


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
    issues: List[dict]
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
    dispatchDate: Optional[datetime]
    carrier: OrderCarrier
    fulfillmentLocation: OrderFulfillmentLocation
    tracking: Optional[OrderTracking]
    items: List[dict]
    status: str


class Address(BaseModel):
    line1: str
    line2: Optional[str] = ''
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
    printArea: str
    md5Hash: Optional[str]
    url: str
    thumbnailUrl: Optional[str] = None
    status: Optional[str] = None


class ItemAssetResponse(ItemAsset):
    id: str


class ItemGeneralStatusEnum(str, Enum):
    ok = 'Ok'
    invalid = 'Invalid'


class SizingEnum(str, Enum):
    fill_print_area = 'fillPrintArea'
    fit_print_area = 'fitPrintArea'
    stretch_to_print_area = 'stretchToPrintArea'


class Item(BaseModel):
    merchantReference: Optional[str]
    sku: str
    copies: int
    sizing: SizingEnum
    thumbnailUrl: Optional[str] = None
    attributes: dict
    assets: List[ItemAsset | ItemAssetResponse]
    recipientCost: Optional[MoneyAmount]
    correlationIdentifier: Optional[str] = None


class ItemResponse(Item):
    id: str
    status: ItemGeneralStatusEnum


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


class OrderBase(BaseModel):
    merchantReference: Optional[str] = None
    shippingMethod: ShippingMethodEnum
    idempotencyKey: Optional[str] = None
    recipient: Recipient
    items: List[Item | ItemResponse]
    packingSlip: Optional[PackingSlip] = None
    metadata: Optional[OrderMetadata]


class Order(OrderBase):
    id: str
    status: OrderStatus
    charges: List[OrderCharge]
    created: datetime
    shipments: List[OrderShipment]
    lastUpdated: datetime
    callbackUrl: Optional[Callback] = None
    charges: List[OrderCharge]


class ListOrderResponse(ResponseCommon):
    orders: List[Order]


class RequestResponse(ResponseCommon):
    order: Order


class YesNoEnum(str, Enum):
    """ It comes like that from prodigi.com go complain with them"""
    yes = "Yes"
    no = "No"


class IsAvailable(BaseModel):
    isAvailable: YesNoEnum


class OrderActionsResponse(ResponseCommon):
    cancel: IsAvailable
    changeRecipientDetails: IsAvailable
    changeShippingMethod: IsAvailable
    changeMetaData: IsAvailable


class CancelOrderResponse(ResponseCommon):
    order: Order


class CostSummary(BaseModel):
    cost: MoneyAmount
    shipping: MoneyAmount


class Quote(BaseModel):
    shipmentMethod: ShippingMethodEnum
    costSummary: CostSummary
    shipments: OrderShipment
    items: Item
