from sqlalchemy import create_engine
from db_model import Base, PizzaTypes
from engine_setup import engine, session
from sqlalchemy.orm import Session


def __row2dict(row):
    '''Converts query row into dict'''
    return dict((col, getattr(row, col)) for col in row.__table__.columns.keys())


def __query2dict(query):
    '''Converts query rows into dict'''
    return [__row2dict(row=row) for row in query]


def get_pizza_types() -> list[dict]:
    '''Returns all pizzas from table PizzaTypes as list of dicts'''
    query = session.query(PizzaTypes)
    return __query2dict(query=query)


def get_pizza_price(id: int) -> int:
    query = session.query(PizzaTypes).filter(PizzaTypes.id == id).all()
    pizza = __query2dict(query=query).pop()
    price = 0
    toppings = pizza['toppings']
    for topping in toppings.values():
        price += topping['price'] * topping['amount']
    return price


def delete_pizza_type(id: int) -> None:
    '''Deletes pizza_type by id'''
    session.query(PizzaTypes).filter(PizzaTypes.id == id).delete()
    session.commit()


if __name__ == "__main__":
    # print(get_pizza_types())
    print(get_pizza_price(id=2))
