FROM python:3.12-bookworm

RUN pip install playwright==@1.48.0 && playwright install --with-deps