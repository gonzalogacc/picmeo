import os

from sqlmodel import create_engine, SQLModel, Session

from settings import Settings

engines = {
    'postgresql': f'postgresql://{Settings.POSTGRES_USER}:{Settings.POSTGRES_PASSWORD}@{Settings.POSTGRES_HOST}:{Settings.POSTGRES_PORT}/{Settings.POSTGRES_DB}',
}

print(f"Connecting to ")
engine = create_engine(engines[Settings.DB_ENGINE])


def drop_tables():
    SQLModel.metadata.drop_all(engine)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine, checkfirst=True)


def get_get_storage() -> Session:
    with Session(engine) as session:
        yield Storage(session)
        session.close()
