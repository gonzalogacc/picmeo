from typing import List

import httpx

from src.prodigi.settings import Settings
from src.prodigi.schema import OrderResponse, RequestResponse, Order, OutcomeEnum

PRODIGI_API_KEY = Settings.PRODIGI_API_KEY
PRODIGI_BASE_URL = Settings.PRODIGI_BASE_URL


class Prodigi:
    def __init__(self):
        self.httpx_client = self._httpx_client()

    @staticmethod
    def _httpx_client():
        return httpx.Client(
            base_url=PRODIGI_BASE_URL,
            headers={
                "X-API-Key": PRODIGI_API_KEY,
                "Content-type": "application/json"
            }
        )

    def get_order(self, order_id: str) -> RequestResponse:
        response = self.httpx_client.get(f'/v4.0/orders/{order_id}')
        assert response.status_code in [200], "Error getting orders"
        return RequestResponse(**response.json())

    def get_orders(self) -> List[OrderResponse]:
        response = self.httpx_client.get('/v4.0/orders')
        print(response.json()['orders'])
        assert response.status_code in [200], "Error getting orders"
        return [OrderResponse(**r) for r in response.json()['orders']]

    def create_order(self, order_data: Order) -> OrderResponse:
        response = self.httpx_client.post(f'/v4.0/orders', content=order_data.model_dump_json())
        print("XXXXXXXXXXXX")
        print(response.text)
        print(response.status_code)
        print("XXXXXXXXXXXX")

        assert response.status_code in [200, 201], "Problem creating order"
        order_response = RequestResponse(**response.json())
        assert order_response.outcome == OutcomeEnum.created, "Order was not created"
        return order_response.order

    def product_details(self, product_code: str):
        """ Get the product details for a particular product code

        :param product_code:
        :return:
        """
        pass

    def upload_image(self):
        """
        Upload the image to a bucket and makes it available for prodigy to download
        :return:
        """
        pass

    def place_order(self):
        pass
# "/v4.0/orders/"
# curl "https://api.sandbox.prodigi.com/v4.0/Orders"
# -X POST -H "X-API-Key: your-rest-api-key" -H "Content-Type: application/json"
# -d
# '
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
