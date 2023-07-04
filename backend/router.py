from fastapi import APIRouter
from backend.database.es_managing import connect_es, search_text

router = APIRouter()


@router.get("/")
def search(text: str):
    connect_es()
    return search_text(text)
