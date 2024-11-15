FROM python:3.12-bookworm

# COPY ./PythonFramework /app/PythonFramework
WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt
RUN playwright install --with-deps

COPY pages /pages
COPY report /report
COPY tests /tests
COPY utilities /utilities

RUN pytest /tests
