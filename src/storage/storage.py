from uuid import UUID

from sqlmodel import SQLModel, Session, select

from src.api.users.schema import User


class UserRecord(SQLModel, table=True):
    id: UUID
    phone_number: str
    name: str


class ImageRecord(SQLModel, table=True):
    id: UUID
    image_url: str
    image_md5: str


class Storage:

    def __init__(self, session: Session):
        self.session = session

    def add_user(self, user: User):
        self.session.add(UserRecord(
            id=user.id,
            phone_number=user.phone_number,
            name=user.name
        ))
        self.session.commit()

    def get_user(self, user_id: UUID) -> UserRecord:
        return self.session.exec(select(UserRecord).where(UserRecord.id == UUID)).one_or_none()
