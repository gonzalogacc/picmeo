from fastapi import APIRouter

from src.api.whatsapp.functions import veryify_webhook


class WhatsappClient:

    def __init__(self):
        self.router = APIRouter()
        self._add_webhooks()

    def _add_webhooks(self):
        webhooks_api = APIRouter(prefix="/v1/webhooks")

        @webhooks_api.get("/")
        def meta_webhooks(request):
            """
            hub.mode=subscribe&hub.challenge=1918437135&hub.verify_token=verificacion
            """
            # try:
            return veryify_webhook(request)

            # except Exception as e:
            #    print(e)
            #    raise HTTPException(status_code=500, detail="Error")

        self.router.include_router(webhooks_api)