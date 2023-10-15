from typing import List

import httpx

from src.prodigi.settings import Settings
from src.prodigi.schema import Order, OrderRequestResponse, OrderBase, OutcomeEnum, OrderActionsResponse, \
    CancelOrderResponse, ListOrderResponse

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

    def get_order(self, order_id: str) -> Order:
        response = self.httpx_client.get(f'/v4.0/orders/{order_id}')
        assert response.status_code in [200], "Error getting orders"
        print(response.json())
        return OrderRequestResponse(**response.json()).order

    def get_orders(self) -> List[Order]:
        response = self.httpx_client.get('/v4.0/orders')
        assert response.status_code in [200], "Error getting orders"
        return ListOrderResponse(**response.json()).orders

    def create_order(self, order_data: OrderBase) -> Order:
        response = self.httpx_client.post(f'/v4.0/orders', content=order_data.model_dump_json())
        assert response.status_code in [200, 201], f"Problem creating order {response.text}"
        order_response = OrderRequestResponse(**response.json())
        assert order_response.outcome == OutcomeEnum.created, "Order was not created"
        return order_response.order

    def get_order_actions(self, order_id: str) -> OrderActionsResponse:
        response = self.httpx_client.get(f'/v4.0/orders/{order_id}/actions')
        assert response.status_code in [200], "Problem reading actions"
        order_actions = OrderActionsResponse(**response.json())
        assert order_actions.outcome == OutcomeEnum.ok, f"Problem reading actions: {order_actions.outcome}"
        return order_actions

    def cancel_order(self, order_id: str) -> CancelOrderResponse:
        response = self.httpx_client.post(f'/v4.0/orders/{order_id}/actions/cancel')
        assert response.status_code in [200, ], "problem deleting order"
        order_cancel = CancelOrderResponse(**response.json())
        assert order_cancel.outcome == OutcomeEnum.cancelled, f"Probelem cancelling order {order_cancel.outcome}"
        return order_cancel

    def upload_image(self):
        """
        Upload the image to a bucket and makes it available for prodigy to download
        :return:
        """
        pass
