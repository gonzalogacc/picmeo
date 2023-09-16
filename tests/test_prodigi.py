from src.prodigi.prodigi import Prodigi
from tests.schema_fixtures import prodigi_test_client

# def test_product_details_parse_object(product_details):
#     pd = ProductDetails(product_details)
#     assert pd.sku == "GLOBAL-CAN-10X10"


def test_get_all_orders(prodigi_test_client):
    pd = Prodigi()
    pd.httpx_client = prodigi_test_client
    response = pd.get_orders()
    print(response)
    assert len(response) > 0


def test_get_order(prodigi_test_client):
    pd = Prodigi()
    pd.httpx_client = prodigi_test_client
    order_id = 'ord_1101519'
    order = pd.get_order(order_id)
    print(order)
    assert order.order.id == order_id