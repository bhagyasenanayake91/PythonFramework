FROM mcr.microsoft.com/playwright/playwright/python:v1.47.0-noble

WORKDIR /app

COPY pages /app/pages
COPY report /app/report
COPY tests /app/tests
COPY utilities /app/utilities

# RUN pip install playwright && \
#     playwright install --with-deps

# RUN pytest
