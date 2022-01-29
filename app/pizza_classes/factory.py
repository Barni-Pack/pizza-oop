from parent import Pizza
import sys
sys.path.append('../../')  # noqa
from database.alchemy import get_pizza_types


PIZZA_CLASSES = []


def pizza_factory(pizza_dict: dict):
    name = pizza_dict['name']
    bases = (Pizza, )
    toppings = pizza_dict['toppings']
    toppings_names = [t_key for t_key, t_value in toppings.items()]
    backing_time = sum([t_value['time']
                       for t_key, t_value in toppings.items()])
    price = sum([t_value['price'] * t_value['amount']
                for t_key, t_value in toppings.items()])
    # print(toppings_names, backing_time, price)
    dict_ = dict(
        toppings=toppings_names,
        backing_time=backing_time,
        price=price,
    )

    return type(name, bases, dict_)


pizza_types = get_pizza_types()
for pizza_type in pizza_types:
    PIZZA_CLASSES.append(pizza_factory(pizza_dict=pizza_type)())

print(PIZZA_CLASSES)


# class PizzaFactory(pizza_dict: dict):


if __name__ == "__main__":
    pass
