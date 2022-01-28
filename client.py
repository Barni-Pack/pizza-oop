from widgets import Widgets
from engine import window, tk
from app.terminal import terminal
from app.pizza_classes import Pizza, Pepperoni, Barbecue, Seafood
from functools import partial
from app import pizza_storage
from config import Offset, Labels

# TODO: adjust window_height to size of pizzas, or make pizza's list scrollable
window_width = 420 + 6 * 10
window_height = 420


window.title('Terminal')
window.geometry(f'{window_width}x{window_height}')
window.resizable(width=False, height=False)

# window.rowconfigure(0, minsize=50, weight=1)
window.columnconfigure(list(range(6)), minsize=50, weight=1)


Widgets.label(**Labels.greetings)


# def update_count_label(pizza: Pizza):
#     pizza_count = len(
#         [p for p in terminal.order.products_list if p == pizza]
#     )
#     print(pizza_count)
#     Widget.label(
#         text=pizza_count,
# **Labels.pizza_count,
#     )
#     # count_label = tk.Label(
#     #     master=window,
#     #     text=pizza_count,
#     # )
#     # count_label.grid(
#     #     row=row_offset,
#     #     column=5,
#     #     sticky='nsew',
#     # )


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
    pizza_in_stock = pizza_storage.get_pizza_amount(pizza_name=pizza_name)
    row_offset = pizza_id + 1

    Widgets.label(
        text=pizza_name + f' ( in stock: {pizza_in_stock} ) :',
        row=row_offset,
        column=0,
        columnspan=2,
    )

    Widgets.label(
        text=pizza.price,
        row=row_offset,
        column=2,
    )

    btn_decrease = tk.Button(
        master=window,
        text="-",
        command=partial(remove_product, pizza)
    )
    btn_increase = tk.Button(
        master=window,
        text="+",
        command=partial(add_product, pizza)
    )

    btn_decrease.grid(
        row=row_offset,
        column=3,
        sticky='nsew',
    )
    btn_increase.grid(
        row=row_offset,
        column=4,
        sticky='nsew',
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
    text='Commit your order!',
    command=commit_order,
    row=len(pizzas) + 2,
    columnspan=4,
    column=1,
)

update_counters()
update_order_price()

window.mainloop()
