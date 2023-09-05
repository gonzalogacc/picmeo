
from src.prodigi.schema import ProductDetails
from tests.schema_fixtures import product_details


def test_product_details_parse_object(product_details):
    pd = ProductDetails(product_details)
    assert pd.sku == "GLOBAL-CAN-10X10"
