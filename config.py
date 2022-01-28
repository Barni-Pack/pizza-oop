class Offset:
    greetings = 0
    order_number = 1


class Labels:
    greetings = dict(
        text='Welcome to Pizza Hub!\nHere is menu:',
        row=Offset.greetings,
        columnspan=6,
        sticky='nsew',
        pady=20,
    )
