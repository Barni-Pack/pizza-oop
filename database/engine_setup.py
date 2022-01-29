from sqlalchemy import create_engine
from sqlalchemy.orm import Session
import sys
sys.path.append('..')  # noqa
from db_config import database_path  # noqa


def engine_setup(path=database_path):
    engine = create_engine(path)
    session = Session(bind=engine)
    return (engine, session)


engine, session = engine_setup()
