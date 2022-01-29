from sqlalchemy import create_engine
from sqlalchemy.orm import Session
# import sys
# sys.path.append('..')  # noqa
# from db_config import database_path  # noqa

database_path = r'sqlite:///C:\\Code\\pizza-oop\\pizza_types.db'

def engine_setup(path=database_path):
    engine = create_engine(path)
    session = Session(bind=engine)
    return (engine, session)


engine, session = engine_setup()
