from fastapi import APIRouter
from backend.database.es_managing import search_text
from backend.database.es_managing import delete_by_id as es_delete
from backend.database.pg_managing import delete_by_id as pg_delete

router = APIRouter()


@router.get("/search/")
def search(text: str):
    return search_text(text)


@router.get("/delete/")
def search(id: str):
    pg_delete(id)
    return es_delete(id)
