FROM python:3.10-slim

WORKDIR /app

ADD pyproject.toml .
RUN pip install poetry
RUN poetry install

ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH=.
ENV PYTHONDONTWRITEBYTECODE 1

COPY ./src .

CMD ["poetry", "run", "python", "src/main.py"]
