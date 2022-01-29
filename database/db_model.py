from sqlalchemy import Column, Integer, String, JSON
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class PizzaTypes(Base):
    __tablename__ = 'pizza_types'
    id = Column(
        Integer,
        nullable=False,
        unique=True,
        primary_key=True,
        autoincrement=True
    )
    name = Column(String(200), nullable=False)
    toppings = Column(JSON, nullable=False)

    # def __repr__(self):
    #     return f'{self.topic_id} {self.name} {self.description}'


if __name__ == "__main__":
    # from engine import engine, session

    pass    
