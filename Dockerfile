FROM python:3.11-buster

RUN apt update -y && apt install uvicorn -y

RUN pip install poetry

COPY . /app/picmeo

WORKDIR /app/picmeo
RUN poetry install

EXPOSE 8080
ENTRYPOINT ["poetry", "run", "python", "run.py"]
