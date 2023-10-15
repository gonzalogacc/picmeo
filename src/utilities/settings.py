from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()

class _Settings(BaseSettings):
    GOOGLE_CREDS: str
    GOOGLE_PROJECT: str = 'static-project-1'
    BUCKET_NAME: str = 'picmeo_images'


Settings = _Settings()
