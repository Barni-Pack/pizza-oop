# import db_config  # noqa
# db_config.database_path = 'sqlite:///database/pizza_types.db'  # noqa
from widgets import Widgets
from engine import window, tk
from app.terminal import terminal
from app.pizza_classes import Pizza, Pepperoni, Barbecue, Seafood
from functools import partial
from database.alchemy import get_pizza_types, delete_pizza_type, get_pizza_price

# TODO: adjust window_height to size of pizzas, or make pizza's list scrollable
window_width = 420 + 6 * 10
window_height = 420


window.title('Terminal')
window.geometry(f'{window_width}x{window_height}')
window.resizable(width=False, height=False)

# window.rowconfigure(0, minsize=50, weight=1)
window.columnconfigure(list(range(6)), minsize=50, weight=1)


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


def redraw(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        # update_counters()
        for widget in window.winfo_children():
            widget.destroy()
        draw_gui()
    return wrapper


@redraw
def delete_pizza_type_command(pizza_id: int):
    delete_pizza_type(id=pizza_id)
    print('nigga')


@redraw
def add_product(pizza: Pizza):
    terminal.order.add_product(product=pizza)


@redraw
def remove_product(pizza: Pizza):
    terminal.order.remove_product(product=pizza)


def draw_gui():
    ROW = 0
    Widgets.label(
        text='Панель администратора',
        row=ROW,
        columnspan=6,
        pady=10,
    )
    ROW += 1

    def get_menu_len(pizzas: list[dict]) -> int:
        menu_len = 0
        l_of_d = [pizza[toppings] for pizza in pizzas]
        menu_len += len(l_of_d)
        for d in l_of_d:
            menu_len += len(d)
        return l_of_d

    pizzas = get_pizza_types()
    for pizza_id, pizza in enumerate(pizzas):
        pizza_name = pizza['name']
        price = get_pizza_price(id=pizza['id']) 
        ROW += 1

        Widgets.label(
            text=pizza_name + ':',
            row=ROW,
            column=0,
            columnspan=2,
        )

        Widgets.label(
            text=f'Цена: {price}',
            row=ROW,
            column=2,
        )

        Widgets.button(
            text="Del",
            command=partial(delete_pizza_type_command, pizza['id']),
            row=ROW,
            column=5,
        )

        def params_string_gen(key, value) -> str:
            string_list = []
            for k, v in value.items():
                string_list.append(str(v))
            return ', '.join(string_list)

        ROW += 1
        Widgets.label(
            text='Начинка',
            row=ROW,
            column=0,
            # columnspan=2,
        )

        Widgets.label(
            text='цена',
            row=ROW,
            column=1,
        )
        Widgets.label(
            text='время',
            row=ROW,
            column=2,
        )
        Widgets.label(
            text='кол-во',
            row=ROW,
            column=3,
        )
        ROW += 1
        toppings = pizza['toppings']
        for topping_id, (key, value) in enumerate(toppings.items()):
            name = key
            params = params_string_gen(key=key, value=value)
            # text = f'{name}: {params}'
            ROW += topping_id + 1
            Widgets.label(
                text=name,
                row=ROW,
                column=0,
                # columnspan=4,
            )
            for i, (k, v) in enumerate(value.items()):
                Widgets.label(
                    text=str(v),
                    row=ROW,
                    column=1+i,
                )
            Widgets.button(
                text="-",
                # command=partial(remove_product, pizza),
                row=ROW,
                column=4,
            )

            Widgets.button(
                text="+",
                # command=partial(add_product, pizza),
                row=ROW,
                column=5,
            )

            # def update_counters():
            #     for pizza_id, pizza in enumerate(pizzas):
            #         row_offset = pizza_id + 1
            #         pizza_count = len(
            #             [p for p in terminal.order.products_list if p == pizza]
            #         )
            #         Widgets.label(
            #             text=pizza_count,
            #             row=row_offset,
            #             column=5,
            #             sticky='nsew',
            #         )

    # def update_order_price():
    #     order_price = terminal.order.get_total_price()
    #     Widgets.label(
    #         text=f'Order total price: {order_price}',
    #         row=len(pizzas) + 1,
    #         columnspan=6,
    #         sticky='nsew',
    #         pady=20,
    #     )

    # @redraw_labels
    # def commit_order():
    #     terminal.order.commit()

    # Widgets.button(
    #     command=commit_order,
    #     row=len(pizzas) + 2,
    #     text='Commit your order!',
    #     columnspan=6,
    # )

    # update_counters()
    # update_order_price()


# def Refresher():
#     global text
#     # text.configure(text=time.asctime())
#     print('nigga')
draw_gui()
#     window.after(1000, Refresher)
# Refresher()
window.mainloop()
