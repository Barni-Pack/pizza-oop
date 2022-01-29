from widgets import Widgets
from engine import window, tk
from app.terminal import terminal
from app.pizza_classes import Pizza, Pepperoni, Barbecue, Seafood
from functools import partial
# from app import pizza_storage
from db_config import Offset

# TODO: adjust window_height to size of pizzas, or make pizza's list scrollable
window_width = 420 + 6 * 10
window_height = 420


window.title('Terminal')
window.geometry(f'{window_width}x{window_height}')
window.resizable(width=False, height=False)

# window.rowconfigure(0, minsize=50, weight=1)
window.columnconfigure(list(range(6)), minsize=50, weight=1)

Widgets.label(
    text='Welcome to Pizza Hub!\nHere is menu:',
    row=Offset.greetings,
    columnspan=6,
    sticky='nsew',
    pady=20,
)


def redraw_labels(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        update_counters()
        update_order_price()
    return wrapper


@redraw_labels
def add_product(pizza: Pizza):
    terminal.order.add_product(product=pizza)


@redraw_labels
def remove_product(pizza: Pizza):
    terminal.order.remove_product(product=pizza)


pizzas = [
    Pepperoni(),
    Barbecue(),
    Seafood(),
]
for pizza_id, pizza in enumerate(pizzas):
    pizza_name = pizza.__class__.__name__
    # pizza_in_stock = pizza_storage.get_pizza_amount(pizza_name=pizza_name)
    row_offset = pizza_id + 1

    Widgets.label(
        text=pizza_name+ ':',
        row=row_offset,
        column=0,
        columnspan=2,
    )

    Widgets.label(
        text=pizza.price,
        row=row_offset,
        column=2,
    )

    Widgets.button(
        text="-",
        command=partial(remove_product, pizza),
        row=row_offset,
        column=3,
    )

    Widgets.button(
        text="+",
        command=partial(add_product, pizza),
        row=row_offset,
        column=4,
    )


def update_counters():
    for pizza_id, pizza in enumerate(pizzas):
        row_offset = pizza_id + 1
        pizza_count = len(
            [p for p in terminal.order.products_list if p == pizza]
        )
        Widgets.label(
            text=pizza_count,
            row=row_offset,
            column=5,
            sticky='nsew',
        )


def update_order_price():
    order_price = terminal.order.get_total_price()
    Widgets.label(
        text=f'Order total price: {order_price}',
        row=len(pizzas) + 1,
        columnspan=6,
        sticky='nsew',
        pady=20,
    )


@redraw_labels
def commit_order():
    terminal.order.commit()


Widgets.button(
    command=commit_order,
    row=len(pizzas) + 2,
    text='Commit your order!',
    columnspan=6,
)

update_counters()
update_order_price()

window.mainloop()
