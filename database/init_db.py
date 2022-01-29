from sqlalchemy import create_engine
from db_model import Base, PizzaTypes
from alchemy import get_pizza_types
from engine_setup import engine, session
from sqlalchemy.orm import Session
from toppings import toppings

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

print(get_pizza_types())

for topping in toppings:
    session.add(topping)
session.commit()

print(get_pizza_types())