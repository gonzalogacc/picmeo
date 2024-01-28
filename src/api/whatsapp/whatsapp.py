import json

from fastapi import APIRouter, Request

from src.api.whatsapp.functions import veryify_webhook
from src.api.whatsapp.schema import WebHookNotification


class WhatsappClient:

    def __init__(self):
        self.router = APIRouter()
        self._add_webhooks()

    def _add_webhooks(self):
        webhooks_api = APIRouter(prefix="/v1/webhooks")

        @webhooks_api.get("/ping")
        def pong():
            return dict(message="pong")

        @webhooks_api.get("/")
        def meta_webhooks(request: Request):
            """
            hub.mode=subscribe&hub.challenge=1918437135&hub.verify_token=verificacion
            """
            # try:
            print(request)
            return veryify_webhook(request)

            # except Exception as e:
            #    print(e)
            #    raise HTTPException(status_code=500, detail="Error")

        @webhooks_api.post("/")
        async def message(request: Request):
            data = json.loads(await request.body())
            print(data)
            return dict(message="OK")
            message = WebHookNotification(**data)
            print(message)
            return dict(message="OK")

        self.router.include_router(webhooks_api)
