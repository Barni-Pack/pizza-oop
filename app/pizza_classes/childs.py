from parent import Pizza
import sys
sys.path.append('../../')  # noqa
from database.alchemy import get_pizza_types


# class Toppings():
#     name: str
#     price: float
#     time: float
    

# Mozzarella = Toppings(
#     name='Mozzarella',
#     price=30,
#     time=2,
# )

pizza_types = get_pizza_types()

print(pizza_types)


# class PizzaFactory(pizza_dict: dict):
    


class Pepperoni(Pizza):
    toppings = [
            'Sausage "Pepperoni"',
            'Mozzarella',
            'Fresh-hearted pepper (black)',
        ]
    backing_time = 2
    price = 450.00
    

class Barbecue(Pizza):
    sause = 'Barbecue'
    toppings = [
            'Onion',
            'Parsley',
            'Chicken breask',
        ]
    backing_time = 2
    price = 250.00
    
    
class Seafood(Pizza):
    toppings = [
            'Tomatoes',
            'Sweet peppers',
            'Olieves',
            'Seafood',
            'Onion',
            'Fresh-hearted pepper (black)',
        ]
    backing_time = 4
    price = 650.00
    
if __name__ == "__main__":
    p1 = Pepperoni()

    print(p1)