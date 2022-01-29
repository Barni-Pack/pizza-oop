from db_model import PizzaTypes

toppings = [
    PizzaTypes(
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
    ),
    PizzaTypes(
        name='Margaret',
        toppings={
            'Tomatoes': {
                'price': 80,
                'time': 2,
                'amount': 4,
            },
            'Mozzarella': {
                'price': 90,
                'time': 2,
                'amount': 1,
            },
            'Basil': {
                'price': 20,
                'time': 2,
                'amount': 2,
            },
        }
    ),
    PizzaTypes(
        name='Caprese',
        toppings={
            'Tomatoes': {
                'price': 80,
                'time': 2,
                'amount': 4,
            },
            'Mozzarella': {
                'price': 90,
                'time': 2,
                'amount': 1,
            },
            'Mushrooms': {
                'price': 90,
                'time': 4,
                'amount': 5,
            },
            'Ham': {
                'price': 60,
                'time': 8,
                'amount': 3,
            },
            'Green Olives': {
                'price': 20,
                'time': 4,
                'amount': 6,
            },
            'Black Olives': {
                'price': 20,
                'time': 4,
                'amount': 6,
            },
        }
    ),
    PizzaTypes(
        name='4 cheeses',
        toppings={
            'Dor Blue Cheese': {
                'price': 80,
                'time': 2,
                'amount': 4,
            },
            'Mozzarella': {
                'price': 80,
                'time': 2,
                'amount': 4,
            },
            'Parmesan': {
                'price': 90,
                'time': 2,
                'amount': 4,
            },
            'Emmental': {
                'price': 100,
                'time': 2,
                'amount': 4,
            },
            'Tomato sauce': {
                'price': 100,
                'time': 4,
                'amount': 1,
            },
        }
    )
]
