from sqlalchemy import create_engine
from sqlalchemy.orm import Session


engine = create_engine('sqlite:///database/pizza_storage.db')
session = Session(bind=engine)
