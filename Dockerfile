FROM python:3.13-bookworm

RUN pip install playwright && playwright install --with-deps && pytest