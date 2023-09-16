from src.prodigi.prodigi import Prodigi
from src.prodigi.schema import Order, ShippingMethodEnum, Recipient, Address, Item, SizingEnum, MoneyAmount, ItemAsset, \
    OrderMetadata, OutcomeEnum
from tests.schema_fixtures import prodigi_test_client


# def test_product_details_parse_object(product_details):
#     pd = ProductDetails(product_details)
#     assert pd.sku == "GLOBAL-CAN-10X10"


def test_get_order(prodigi_test_client):
    pd = Prodigi()
    pd.httpx_client = prodigi_test_client
    order_id = 'ord_1101519'
    order = pd.get_order(order_id)
    print(order)
    assert order.order.id == order_id


def test_get_all_orders(prodigi_test_client):
    pd = Prodigi()
    pd.httpx_client = prodigi_test_client
    response = pd.get_orders()
    print(response)
    print(len(response))
    assert len(response) > 0


def test_create_order(prodigi_test_client):
    pd = Prodigi()
    pd.httpx_client = prodigi_test_client
    recipient = Recipient(
        name='Mr Test',
        email=None,
        phoneNumber=None,
        address=Address(
            line1='14 test place',
            line2='test',
            postalOrZipCode='12345',
            townOrCity='somewhere',
            countryCode='US'
        )
    )
    item = Item(
        merchantReference="Item uno",
        sku="GLOBAL-CFPM-16X20",
        copies=1,
        sizing=SizingEnum.fill_print_area,
        attributes=dict(color='black'),
        recipientCost=MoneyAmount(amount='50', currency='USD'),
        assets=[ItemAsset(
            printArea='default',
            url="https://pwintyimages.blob.core.windows.net/samples/stars/test-sample-grey.png",
            md5Hash="daa1c811c6038e718a23f0d816914b7b"
        )],
    )
    order_metadata = OrderMetadata(
        mycustomkey="some-guid",
        someCustomerPreference=dict(
            preference1="something",
            preference2="red",
            sourceId=12345
        )
    )
    order_data = Order(
        merchantReference="MyMerchantReference1",
        shippingMethod=ShippingMethodEnum.overnight,
        recipient=recipient,
        items=[item],
        metadata=order_metadata
    )

    response = pd.create_order(order_data)
    print(response)

    assert response.id == 'ord_840797'

def test_get_order_actions(prodigi_test_client):
    pd = Prodigi()
    pd.httpx_client = prodigi_test_client
    action_id = "ord_1101519"
    actions = pd.get_order_actions(action_id)
    assert actions.cancel.isAvailable == "No"

def test_cancel_order_action(prodigi_test_client):
    pd = Prodigi()
    pd.httpx_client = prodigi_test_client
    order_id = "ord_1101519"
    action = pd.cancel_order(order_id)
    assert action.outcome == OutcomeEnum.cancelled
