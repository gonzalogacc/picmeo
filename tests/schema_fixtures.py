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

def get_order_actions_dummy(request: Request):
    return _response_from_file('prodigi_sample_responses/get_order_actions.json')

@pytest.fixture(scope="session")
def prodigi_test_client():
    app = Starlette(routes=[
        # Route('/v4.0/orders', get_orders_dummy),
        Route('/v4.0/orders/{order_id:str}', get_order_dummy),
        Route('/v4.0/orders', post_order_dummy, methods=['POST']),
        Route('/v4.0/orders/{order_id:str}/actions', get_order_actions_dummy)
    ])
    return TestClient(app)
