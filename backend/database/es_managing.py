from sqlalchemy.orm import Session
from elasticsearch import Elasticsearch
from backend.database.pg_managing import engine, Base, Page

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
        connect_es()
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


def delete_by_id(id_del: str):
    if not es.indices.exists(index=INDEX_NAME):
        connect_es()

    body = {
        "size": 1,
        "query": {
            "match": {
                "id": id_del
            }
        }
    }

    es_obj = es.search(index=INDEX_NAME, body=body)["hits"]["hits"]

    if not es_obj:
        return "No such element"

    es.delete(index=INDEX_NAME, id=es_obj[0]['_id'])
    return f"Deleted id:{id_del}"
