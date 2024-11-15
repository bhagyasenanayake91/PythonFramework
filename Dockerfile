# FROM python:3.13-bookworm

# RUN pip install playwright 

# RUN playwright install --with-deps

# # RUN pytest

FROM mcr.microsoft.com/playwright/python:v1.47.0-noble

WORKDIR /app

COPY pages /app/pages
COPY report /app/report
COPY tests /app/tests
COPY utilities /app/utilities

RUN pip install playwright==@1.47.0 && \
    playwright install --with-deps