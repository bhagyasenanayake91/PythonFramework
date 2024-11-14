FROM python:3.13-bookworm

RUN pip install playwright 

# RUN pip playwright install --with-deps

RUN pip pytest