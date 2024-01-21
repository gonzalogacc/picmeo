import pytest

from src.api.whatsapp.functions import veryify_webhook
from src.api.whatsapp.schema import VerificationException, MissingParametersException


def test_verify_webhook():
    class Request:
        def __init__(self):
            self.query_params = {
                "hub.mode": "subscribe",
                "hub.challenge": 1000,
                "hub.verify_token": "verif"
            }

    req = Request()
    challenge = veryify_webhook(req)
    assert challenge == 1000

    # Bad verification token
    req.query_params['hub.verify_token'] = 'malo'
    with pytest.raises(VerificationException):
        veryify_webhook(req)


    # Missing params
    req = Request()
    req.query_params.pop('hub.challenge')
    with pytest.raises(MissingParametersException):
        veryify_webhook(req)
