import db_config  # noqa
db_config.database_path = 'sqlite:///database/pizza_types.db'  # noqa
from widgets import Widgets
from engine import window, tk
from app.terminal import terminal
from app.pizza_classes import Pizza
from app.pizza_classes.factory import PIZZA_CLASSES
from functools import partial
from database.alchemy import get_pizza_types, get_pizza_price

# TODO: adjust window_height to size of pizzas, or make pizza's list scrollable
window_width = 420 + 6 * 10
window_height = 420


window.title('Terminal')
window.geometry(f'{window_width}x{window_height}')
window.resizable(width=False, height=False)

# window.rowconfigure(0, minsize=50, weight=1)
window.columnconfigure(list(range(6)), minsize=50, weight=1)


print(PIZZA_CLASSES)

def redraw(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        # update_counters()
        for widget in window.winfo_children():
            widget.destroy()
        draw_gui()
    return wrapper


@redraw
def add_product(pizza: Pizza):
    terminal.order.add_product(product=pizza)


@redraw
def remove_product(pizza: Pizza):
    terminal.order.remove_product(product=pizza)


@redraw
def commit_order():
    terminal.order.commit()


def draw_gui():
    ROW = 0
    Widgets.label(
        text='Добро пожаловать на Pizza Hub!\nСоберите заказ из меню:',
        row=ROW,
        columnspan=6,
        pady=10,
    )
    ROW += 1

    for pizza_id, pizza in enumerate(PIZZA_CLASSES):
        pizza_name = pizza.__class__.__name__
        price = pizza.price
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
            text="-",
            command=partial(remove_product, pizza),
            row=ROW,
            column=3,
        )

        Widgets.button(
            text="+",
            command=partial(add_product, pizza),
            row=ROW,
            column=4,
        )

        pizza_count = len(
            [p for p in terminal.order.products_list if p == pizza]
        )
        Widgets.label(
            text=pizza_count,
            row=ROW,
            column=5,
            sticky='nsew',
        )
    ROW += 1

    order_price = terminal.order.get_total_price()
    Widgets.label(
        text=f'Order total price: {order_price}',
        row=ROW,
        columnspan=6,
        sticky='nsew',
        pady=20,
    )
    ROW += 1

    Widgets.button(
        command=commit_order,
        row=ROW,
        text='Commit your order!',
        columnspan=6,
    )


draw_gui()
window.mainloop()
