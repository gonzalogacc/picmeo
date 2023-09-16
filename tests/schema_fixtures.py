import json

import pytest

from httpx import Request
from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route
from starlette.testclient import TestClient


def _response_from_file(filename: str) -> JSONResponse:
    data = json.loads(open(filename).read())
    return JSONResponse(data)


def get_orders_dummy(request: Request):
    return _response_from_file('prodigi_sample_responses/get_orders.json')

def get_order_dummy(request: Request):
    return _response_from_file('prodigi_sample_responses/get_order_ord_1101519.json')

def post_order_dummy(request: Request):
    return _response_from_file('prodigi_sample_responses/create_order_ord.json')

@pytest.fixture(scope="session")
def prodigi_test_client():
    app = Starlette(routes=[
        # Route('/v4/orders', get_orders_dummy),
        Route('/v4/orders/{order_id:str}', get_order_dummy),
        Route('/v4/orders', post_order_dummy, methods=['POST']),
    ])
    return TestClient(app)


@pytest.fixture
def product_details():
    return {"sku": "GLOBAL-CAN-10X10",
            "description": "Standard canvas on quality stretcher bar, 25x25cm",
            "productDimensions": {
                "width": 10.0000,
                "height": 10.0000,
                "units": "in"
            },
            "attributes": {
                "wrap": [
                    "Black",
                    "ImageWrap",
                    "MirrorWrap",
                    "White"
                ]
            },
            "printAreas": {
                "default": {
                    "required": true
                }
            },
            "variants": [
                {
                    "attributes": {
                        "wrap": "Black"
                    },
                    "shipsTo": [
                        "IM",
                        "LU",
                        "ID",
                        "CI",
                        "GR",
                        "FK",
                        "AL",
                        "LA",
                        "KY"
                    ],
                    "printAreaSizes": {
                        "default": {
                            "horizontalResolution": 1522,
                            "verticalResolution": 1522
                        }
                    }
                },
                {
                    "attributes": {
                        "wrap": "ImageWrap"
                    },
                    "shipsTo": [
                        "IM",
                        "LU",
                        "ID",
                        "CI",
                        "GR",
                        "FK",
                        "AL",
                        "LA",
                        "KY"
                    ],
                    "printAreaSizes": {
                        "default": {
                            "horizontalResolution": 2137,
                            "verticalResolution": 2137
                        }
                    }
                },
                {
                    "attributes": {
                        "wrap": "MirrorWrap"
                    },
                    "shipsTo": [
                        "IM",
                        "LU",
                        "ID",
                        "CI",
                        "GR",
                        "FK",
                        "AL",
                        "LA",
                        "KY"
                    ],
                    "printAreaSizes": {
                        "default": {
                            "horizontalResolution": 1522,
                            "verticalResolution": 1522
                        }
                    }
                },
                {
                    "attributes": {
                        "wrap": "White"
                    },
                    "shipsTo": [
                        "IM",
                        "LU",
                        "ID",
                        "CI",
                        "GR",
                        "FK",
                        "AL",
                        "LA",
                        "KY"
                    ],
                    "printAreaSizes": {
                        "default": {
                            "horizontalResolution": 1522,
                            "verticalResolution": 1522
                        }
                    }
                }
            ]
            }
