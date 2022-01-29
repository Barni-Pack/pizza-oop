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

if __name__ == "__main__":
    engine = create_engine('sqlite:///pizza_storage.db')
    session = Session(bind=engine)
    print(get_pizza_types())
    
    
    # Base.metadata.drop_all(engine)
    # Base.metadata.create_all(engine)

    # p1 = PizzaTypes(
    #     name='Pepperoni',
    #     toppings={
    #         'Mozzarella': {
    #             'price': 10,
    #             'time': 1,
    #             'amount': 2,
    #         },
    #         'Tomato': {
    #             'price': 30,
    #             'time': 3,
    #             'amount': 1,
    #         },
    #         'Sausage': {
    #             'price': 50,
    #             'time': 4,
    #             'amount': 1,
    #         },
    #     }
    # )
    # p1 = PizzaTypes(
    #     name='Carbanara',
    #     toppings={
    #         'Topping 1': {
    #             'price': 50,
    #             'time': 1,
    #             'amount': 2,
    #         },
    #         't2': {
    #             'price': 30,
    #             'time': 1,
    #             'amount': 1,
    #         },
    #         't3': {
    #             'price': 30,
    #             'time': 4,
    #             'amount': 7,
    #         },
    #     }
    # )
    # session.add_all([p1])
    # session.commit()