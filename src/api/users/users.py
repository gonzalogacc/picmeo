from uuid import UUID

from src.api.users.schema import User
from src.storage.storage import Storage


class UserObj:

    def __init__(self, storage: Storage):
        self.storage = storage

    def create_user(self, phone_number: str, name: str) -> User:
        user = User(name=name, phone_number=phone_number)
        self.storage.add_user(user)
        return user

    def get_user(self, user_id: UUID) -> User:
        return User(**self.storage.get_user(user_id))
