from sqlalchemy import String, Column, Integer, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()


class Page(Base):
    __tablename__ = "page"
    id = Column("id", Integer, primary_key=True)
    text = Column("text", String, nullable=False)
    date_creation = Column("date_creation", TIMESTAMP, default=datetime.utcnow)
    rubrics = Column("rubrics", String)
