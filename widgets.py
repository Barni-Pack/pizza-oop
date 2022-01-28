from distutils import command
from engine import window, tk
import functools


WIDGETS = dict()


class Widgets:
    def _widget(
        __tk_object,
        text: str,
        row: int,
        column: int = None,
        command = None,
        sticky='nsew',
        **kwargs,
    ) -> None:
        '''Creates and places with grid new label'''
        global WIDGETS

        # Add column to kwrags because it can be None
        kwargs.update(dict(
            column=column,
        ))
        # Filter None values from dict
        {k: v for k, v in kwargs.items() if v is not None}
        # (row_column) is id of widget
        widget_key = f'{row}_{column if column else None}'

        # tk_object_kwargs = dict(
        #     master=window,
        #     text=text,
        # )

        # if __tk_object == tk.Button:
        #     tk_object_kwargs.update(dict(command=command))
        #     kwargs.pop('command')
        # elif __tk_object == tk.Label:
        #     pass

        # WIDGETS[widget_key] = __tk_object(
        #     **tk_object_kwargs,
        # )
        # WIDGETS[widget_key].grid(
        #     row=row,
        #     sticky=sticky,
        #     **kwargs,
        # )

        if __tk_object == tk.Button:
            WIDGETS[widget_key] = __tk_object(
                master=window,
                text=text,
                command=command,
            )
        elif __tk_object == tk.Label:
            WIDGETS[widget_key] = __tk_object(
                master=window,
                text=text,
            )

        WIDGETS[widget_key].grid(
            row=row,
            sticky=sticky,
            **kwargs,
        )

    label = functools.partial(_widget, tk.Label)
    button = functools.partial(_widget, tk.Button)