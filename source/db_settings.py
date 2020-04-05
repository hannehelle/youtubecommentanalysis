from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.session import sessionmaker

from source.settings import DB_URI


def init_db():
    db = create_engine(DB_URI)
    Base = declarative_base(bind=db)
    Base.metadata.create_all()
    return db, Base


db, Base = init_db()
session_maker = sessionmaker(db)
