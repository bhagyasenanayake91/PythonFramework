# FROM python:3.13-bookworm

# RUN pip install playwright 

# RUN playwright install --with-deps

# # RUN pytest

FROM mcr.microsoft.com/playwright/python:latest

WORKDIR /app

COPY pages /app/pages
COPY report /app/report
COPY tests /app/tests
COPY utilities /app/utilities

RUN pip install playwright && \
    playwright install --with-deps