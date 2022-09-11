FROM python:3.9-slim

WORKDIR /app

ADD pyproject.toml .
RUN pip install poetry
RUN poetry install

ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH=.
ENV PYTHONDONTWRITEBYTECODE 1

COPY ./src ./src

CMD ["poetry", "run", "python", "/app/src/main.py"]
