from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv

load_dotenv()

class _Settings(BaseSettings):
    PRODIGI_API_KEY: str
    PRODIGI_BASE_URL: str

Settings = _Settings()
