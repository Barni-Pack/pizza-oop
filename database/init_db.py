from sqlalchemy import create_engine
from db_model import Base, PizzaTypes
from alchemy import get_pizza_types
from engine_setup import engine, session
from sqlalchemy.orm import Session

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

print(get_pizza_types())

p1 = PizzaTypes(
    name='Pepperoni',
    toppings={
        'Mozzarella': {
            'price': 10,
            'time': 1,
            'amount': 2,
        },
        'Tomato': {
            'price': 30,
            'time': 3,
            'amount': 1,
        },
        'Sausage': {
            'price': 50,
            'time': 4,
            'amount': 1,
        },
    }
)
p2 = PizzaTypes(
    name='Carbanara',
    toppings={
        'Topping 1': {
            'price': 50,
            'time': 1,
            'amount': 2,
        },
        't2': {
            'price': 30,
            'time': 1,
            'amount': 1,
        },
        't3': {
            'price': 30,
            'time': 4,
            'amount': 7,
        },
    }
)
session.add_all([p1, p2])
session.commit()

print(get_pizza_types())