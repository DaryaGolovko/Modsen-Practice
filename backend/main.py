from backend.database.es_managing import connect_es, search_text, es
from fastapi import FastAPI
import uvicorn
"""
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(BASE_DIR, ".env"))
"""
app = FastAPI(
    title="Text searcher"
)

@app.get("/")
def startup():
    return "Lets start!"


@app.get("/search/{query}")
def search(query: str):
    return search_text(query)

#app.add_middleware(DBSessionMiddleware, db_url=os.environ["DATABASE_URL"])


if __name__ == "__main__":
    connect_es()
    #uvicorn.run(app, host="127.0.0.1", port=8000)
