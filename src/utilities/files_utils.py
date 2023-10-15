import hashlib
import os
import sys
import urllib.parse
import uuid

from google.cloud import storage
from google.oauth2 import service_account

from settings import Settings

credentials = service_account.Credentials.from_service_account_file(Settings.GOOGLE_CREDS)


def upload_blob(source_file_name: str):
    """Uploads a file to the bucket."""
    extension = os.path.splitext(source_file_name)[-1]
    if extension not in ['.png', '.jpg']:
        raise Exception("Invalid filetype")

    storage_client = storage.Client(project=Settings.GOOGLE_PROJECT, credentials=credentials)
    bucket = storage_client.bucket(Settings.BUCKET_NAME)

    destination_blob_name = f'image_{str(uuid.uuid4())}{extension}'
    blob = bucket.blob(destination_blob_name)

    image = open(source_file_name, 'rb').read()
    generation_match_precondition = 0
    blob.upload_from_string(image, if_generation_match=generation_match_precondition)
    print(f"File {source_file_name} uploaded to {destination_blob_name}.")

    BASE_URL = "https://storage.googleapis.com"
    url_path = f'{Settings.BUCKET_NAME}/{destination_blob_name}'
    md5sum = hashlib.md5(image).hexdigest()
    return urllib.parse.urljoin(BASE_URL, url_path), md5sum


if __name__ == "__main__":
    print(f'Uploading file')
    image_url, md5 = upload_blob(sys.argv[1])
    print(f'File uploaded to: {image_url} : {md5}')
