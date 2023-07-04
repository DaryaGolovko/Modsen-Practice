import os
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from elasticsearch import Elasticsearch
from dotenv import load_dotenv
from backend.database.pg_managing import *

load_dotenv()

DB_HOST = os.environ.get("DB_HOST")
DB_NAME = os.environ.get("DB_NAME")
DB_USER = os.environ.get("DB_USER")
DB_PASS = os.environ.get("DB_PASS")

DB_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}"

engine = create_engine(DB_URL, echo=True)

es = Elasticsearch("http://localhost:9200")

INDEX_NAME = "page"


def connect_es():
    if not es.indices.exists(index=INDEX_NAME):
        es_index = {
            "mappings": {
                "properties": {
                    "id": {"type": "integer"},
                    "text": {"type": "text"}
                }
            }
        }
        es.indices.create(index=INDEX_NAME, body=es_index, ignore=[400])

        Base.metadata.create_all(bind=engine)

        with Session(autoflush=False, bind=engine) as db:
            pages = db.query(Page).all()
            for p in pages:
                id = p.id
                text = p.text

                body = {
                    'id': id,
                    'text': text
                }
                es.index(index=INDEX_NAME, body=body)


def search_text(text: str):
    if not es.indices.exists(index=INDEX_NAME):
        return "no data"
    result = es.search(index=INDEX_NAME, body={
        "size": 20,
        "query": {
            "match": {
                'text': text
            }
        }
    })
    result_ids = [[item["_source"]["id"], item["_source"]["text"]] for item in result["hits"]["hits"]]
    return result_ids
