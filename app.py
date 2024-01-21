from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.api.whatsapp.whatsapp import WhatsappClient

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

whatsapp_client = WhatsappClient()
app.include_router(whatsapp_client.router)

# @app.get("/")
# def index():
#     return "OK"