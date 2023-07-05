from sqlalchemy import String, Column, Integer, TIMESTAMP, delete
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from dotenv import load_dotenv
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

load_dotenv()

DB_HOST = os.environ.get("DB_HOST")
DB_NAME = os.environ.get("DB_NAME")
DB_USER = os.environ.get("DB_USER")
DB_PASS = os.environ.get("DB_PASS")

TABLE_NAME = "page"

DB_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}"

engine = create_engine(DB_URL, echo=True)

Base = declarative_base()


class Page(Base):
    __tablename__ = TABLE_NAME
    id = Column("id", Integer, primary_key=True)
    text = Column("text", String, nullable=False)
    date_creation = Column("date_creation", TIMESTAMP, default=datetime.utcnow)
    rubrics = Column("rubrics", String)


def delete_by_id(id_del: str):
    Base.metadata.create_all(bind=engine)

    with Session(autoflush=False, bind=engine) as db:
        pg_obj = delete(Page).where(Page.id == id_del)
        db.execute(pg_obj)
        db.commit()
