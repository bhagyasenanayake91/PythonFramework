FROM mcr.microsoft.com/playwright/python:latest

# WORKDIR /app

# COPY pages /app/pages
# COPY report /app/report
# COPY tests /app/tests
# COPY utilities /app/utilities

RUN pip install playwright && \
    playwright install --with-deps
