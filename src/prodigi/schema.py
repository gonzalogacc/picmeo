from enum import Enum
from typing import List

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
    shipsTo: List[ShipsToEnum]
    printAreaSizes: VariantPrintAreaSizes


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


class OrderOUT(BaseModel):
    pass
    # {
    #     "shippingMethod": "Budget",
    #     "recipient": {
    #         "address": {
    #             "line1": "14 test place",
    #             "line2": "test",
    #             "postalOrZipCode": "12345",
    #             "countryCode": "US",
    #             "townOrCity": "somewhere",
    #             "stateOrCounty": "somewhereelse"
    #         },
    #         "name": "John Testman",
    #         "email": "jtestman@prodigi.com"
    #     },
    #     "items": [
    #         {
    #             "sku": "GLOBAL-FAP-16x24",
    #             "copies": 1,
    #             "sizing": "fillPrintArea",
    #             "assets": [
    #                 {
    #                     "printArea": "default",
    #                     "url": "https://your-image-url/image.png"
    #                 }
    #             ]
    #         }
    #     ]
    # }


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
