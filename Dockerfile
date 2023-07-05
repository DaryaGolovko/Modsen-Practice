FROM python:3.9

WORKDIR /searcher

COPY ./backend/requirements.txt /searcher/backend/requirements.txt

RUN pip install -r /searcher/backend/requirements.txt

COPY ./backend /searcher/backend

#CMD uvicorn backend.main:app --reload
