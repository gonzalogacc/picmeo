FROM python:3.11-buster

RUN pip install poetry

COPY . /app/picmeo
COPY pyproject.toml /app
COPY poetry.lock /app

WORKDIR /app/picmeo
RUN poetry install

EXPOSE 8080
CMD ["poetry", "run", "python", "/app/picmeo/run.py"]
