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

    #            "attributes": {
    #                "wrap": "Black"
    #            },


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

    #    "variants": [
    #            "printAreaSizes": {
    #                "default": {
    #                    "horizontalResolution": 1522,
    #                    "verticalResolution": 1522
    #                }
    #            }
    #        },
    #        {
    #            "attributes": {
    #                "wrap": "ImageWrap"
    #            },
    #            "shipsTo": [
    #                "IM",
    #                "LU",
    #                "ID",
    #                "CI",
    #                "GR",
    #                "FK",
    #                "AL",
    #                "LA",
    #                "KY"
    #            ],
    #            "printAreaSizes": {
    #                "default": {
    #                    "horizontalResolution": 2137,
    #                    "verticalResolution": 2137
    #                }
    #            }
    #        },
    #        {
    #            "attributes": {
    #                "wrap": "MirrorWrap"
    #            },
    #            "shipsTo": [
    #                "IM",
    #                "LU",
    #                "ID",
    #                "CI",
    #                "GR",
    #                "FK",
    #                "AL",
    #                "LA",
    #                "KY"
    #            ],
    #            "printAreaSizes": {
    #                "default": {
    #                    "horizontalResolution": 1522,
    #                    "verticalResolution": 1522
    #                }
    #            }
    #        },
    #        {
    #            "attributes": {
    #                "wrap": "White"
    #            },
    #            "shipsTo": [
    #                "IM",
    #                "LU",
    #                "ID",
    #                "CI",
    #                "GR",
    #                "FK",
    #                "AL",
    #                "LA",
    #                "KY"
    #            ],
    #            "printAreaSizes": {
    #                "default": {
    #                    "horizontalResolution": 1522,
    #                    "verticalResolution": 1522
    #                }
    #            }
    #        }
    #    ]
    # }


class Order(BaseModel):
    pass
    # {
    #     "merchantReference": "MyMerchantReference1",
    #     "shippingMethod": "Overnight",
    #     "recipient": {
    #         "name": "Mr Testy McTestface",
    #         "address": {
    #             "line1": "14 test place",
    #             "line2": "test",
    #             "postalOrZipCode": "12345",
    #             "countryCode": "US",
    #             "townOrCity": "somewhere",
    #             "stateOrCounty": null
    #         }
    #     },
    #     "items": [
    #         {
    #             "merchantReference": "item #1",
    #             "sku": "GLOBAL-CFPM-16X20",
    #             "copies": 1,
    #             "sizing": "fillPrintArea",
    #             "attributes": {
    #                 "color": "black"
    #             },
    #             "recipientCost": {
    #                 "amount": "15.00",
    #                 "currency": "USD"
    #             },
    #             "assets": [
    #                 {
    #                     "printArea": "default",
    #                     "url": "https://pwintyimages.blob.core.windows.net/samples/stars/test-sample-grey.png",
    #                     "md5Hash": "daa1c811c6038e718a23f0d816914b7b"
    #                 }
    #             ]
    #         }
    #     ],
    #     "metadata": {
    #         "mycustomkey":"some-guid",
    #         "someCustomerPreference": {
    #             "preference1": "something",
    #             "preference2": "red"
    #         },
    #         "sourceId": 12345
    #     }
    # }


class OrderStatusDetails(BaseModel):
    downloadAssets: str
    printReadyAssetsPrepared: str
    allocateProductionLocation: str
    inProduction: str
    shipping: str


class OrderStatus(BaseModel):
    stage: str
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


class ItemAttributes(BaseModel):
    color: "str"


class ItemAsset(BaseModel):
    id: str
    printArea: str
    md5Hash: str
    url: str
    thumbnailUrl: str
    status: str


class Item(BaseModel):
    id: str
    status: str
    merchantReference: str
    sku: str
    copies: int
    sizing: str
    thumbnailUrl: str
    attributes: ItemAttributes
    assets: List[ItemAsset]
    recipientCost: MoneyAmount
    correlationIdentifier: str


class OrderMetadata(BaseModel):
    mycustomkey: str
    someCustomerPreference: dict


class OrderResponse(BaseModel):
    id: str
    created: datetime
    lastUpdated: datetime
    callbackUrl: Optional[str] = None
    merchantReference: Optional[str]
    shippingMethod: str
    idempotencyKey: Optional[str] = None
    status: OrderStatus
    charges: List[OrderCharge]
    shipments: List[OrderShipment]
    recipient: Recipient
    items: List[Item]
    packingSlip: Optional[str] = None
    metadata: OrderMetadata


class RequestResponse(BaseModel):
    outcome: str
    order: OrderResponse
    traceParent: str


class OrderIN(BaseModel):
    pass
#     {
#         "id": "ord_840796",
#         "created": "2021-03-11T14:31:23.41Z",
#         "lastUpdated": "2021-03-11T14:31:23.4931606Z",
#         "callbackUrl": null,
#         "merchantReference": "MyMerchantReference1",
#         "shippingMethod": "Overnight",
#         "idempotencyKey": null,
#         "status": {
#             "stage": "InProgress",
#             "issues": [],
#             "details": {
#                 "downloadAssets": "NotStarted",
#                 "printReadyAssetsPrepared": "NotStarted",
#                 "allocateProductionLocation": "NotStarted",
#                 "inProduction": "NotStarted",
#                 "shipping": "NotStarted"
#             }
#         },
#         "charges": [],
#         "shipments": [],
#         "recipient": {
#             "name": "Mr test",
#             "email": null,
#             "phoneNumber": null,
#             "address": {
#                 "line1": "14 test place",
#                 "line2": "test",
#                 "postalOrZipCode": "12345",
#                 "countryCode": "US",
#                 "townOrCity": "somewhere",
#                 "stateOrCounty": null
#             }
#         },
#         "items": [
#             {
#                 "id": "ori_926886",
#                 "status": "NotYetDownloaded",
#                 "merchantReference": "item #1",
#                 "sku": "GLOBAL-CFPM-16X20",
#                 "copies": 1,
#                 "sizing": "fillPrintArea",
#                 "attributes": {
#                     "color": "black"
#                 },
#                 "assets": [
#                     {
#                         "id": "ast_114059",
#                         "printArea": "default",
#                         "md5Hash": "daa1c811c6038e718a23f0d816914b7b",
#                         "url": "https://pwintyimages.blob.core.windows.net/samples/stars/test-sample-grey.png",
#                         "status": "InProgress"
#                     }
#                 ],
#                 "recipientCost": {
#                     "amount": "10.74",
#                     "currency": "GBP"
#                 }
#             }
#         ],
#         "packingSlip": null,
#         "metadata": {
#             "mycustomkey": "some-guid",
#             "someCustomerPreference": {
#                 "preference1": "something",
#                 "preference2": "red"
#             },
#             "sourceId": 12345
#         }
