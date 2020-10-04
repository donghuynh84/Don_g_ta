import tkinter as tk
from tkinter import ttk
from random import randint
import random
from tkinter import IntVar
from tkinter import messagebox
import tkinter.font as font



# -- Windows only configuration --
try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass
# -- End Windows only configuration --

COLOUR_PRIMARY = "#2e3f4f"
COLOUR_SECONDARY = "#293846"
COLOUR_LIGHT_BACKGROUND = "#e797e8"
COLOUR_LIGHT_TEXT = "#eee"
COLOUR_DARK_TEXT = "#8095a8"
COLOUR_BUTTON_NORMAL = "#5fba7d"
COLOUR_BUTTON_ACTIVE = "#58c77c"
COLOUR_BUTTON_PRESSED = "#44e378"

QUIT_BUTTON_NORMAL = "#4f79db"
QUIT_BUTTON_ACTIVE = "#2f7bf5"
QUIT_BUTTON_PRESSED = "#a81502"


class MathCalculation(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Math for Ava (c) by Don_g_ta")
        self.frames = dict()
        container = ttk.Frame(self)
        container.grid(padx=10, pady=10, sticky="EW")

        for FrameClass in (AddCalculation, Substract):
            frame = FrameClass(container, self)
            self.frames[FrameClass] = frame
            frame.grid(row=1, column=0, sticky="NSEW")
        self.show_frame(AddCalculation)



    def show_frame(self, container):
        frame = self.frames[container]
        self.bind("<Return>", frame.calculate)
        self.bind("<KP_Enter>", frame.calculate)
        frame.tkraise()


class AddCalculation(ttk.Frame):
    def __init__(self, container, controller):
        super().__init__(container)

        self.a_value = tk.IntVar(value=random.randint(1, 50))
        self.b_value = tk.IntVar(value=random.randint(1,20))

        self.answer_value = tk.IntVar()
        first_label = ttk.Label(self, width=19, textvariable=self.a_value, style="MyLabel.TLabel")
        operator_label = ttk.Label(self, width=19, text="ADD", style="MyLabel.TLabel")
        second_label = ttk.Label(self, width=11, textvariable=self.b_value, style="MyLabel.TLabel")
        answer_input = ttk.Entry(self, width=18, textvariable=self.answer_value)
        first_label.grid(column=0, row=0, sticky="E")
        operator_label.grid(column=1, row=0, sticky="E")
        second_label.grid(column=2, row=0, sticky="E")
        answer_input.grid(column=3, row=0, sticky="E")
        answer_input.delete(0, "end")
        answer_input.focus()

        generate_random = ttk.Button(
            self, text="Next",
            command=self.getrandom,
            style="GenerateButton.TButton",
        )
        generate_random.grid(column=2, row=2, sticky="EW")

        calculate_button = ttk.Button(
            self,
            text="Calculate",
            command=self.calculate,
            style="GenerateButton.TButton",

        )
        calculate_button.grid(column=1, row=2, sticky="EW")

        quit_button = ttk.Button(
            self,
            text="Quit",
            command=self.quit,
            style="QuitButton.TButton",
        )
        quit_button.grid(column=4, row=2, sticky="EW")

        switch_page_button = ttk.Button(
            self,
            text="Substract",
            style="GenerateButton.TButton",
            command=lambda: controller.show_frame(Substract)
        )

        switch_page_button.grid(row=2, column=3, sticky="EW")


    def calculate(self, *args):

        a = self.a_value.get()
        b = self.b_value.get()
        c = a + b
        if c == self.answer_value.get():
            print(tk.messagebox.showinfo(title=(f"Answer", {self.answer_value.get()}),
                                         message="You are correct"))
        else:
            print(tk.messagebox.showinfo(title=(f"Answer ", {self.answer_value.get()}),
                                         message="You are not correct"))

    def getrandom(self):
        self.a_value.set(random.randint(1, 50))
        self.b_value.set(random.randint(1, 20))

class Substract(ttk.Frame):
    def __init__(self, container, controller):
        super().__init__(container)

        self.a_value = tk.IntVar(value=random.randint(21, 51))
        self.b_value = tk.IntVar(value=random.randint(1, 20))

        self.answer_value = tk.IntVar()
        first_label = ttk.Label(self, width=19, textvariable=self.a_value, style="MyLabel.TLabel")
        operator_label = ttk.Label(self, width=19, text="MINUS", style="MyLabel.TLabel")
        second_label = ttk.Label(self, width=11, textvariable=self.b_value, style="MyLabel.TLabel")
        answer_input = ttk.Entry(self, width=18, textvariable=self.answer_value)
        first_label.grid(column=0, row=0, sticky="E")
        operator_label.grid(column=1, row=0, sticky="E")
        second_label.grid(column=2, row=0, sticky="E")
        answer_input.grid(column=3, row=0, sticky="E")
        answer_input.delete(0, "end")
        answer_input.focus()

        generate_random = ttk.Button(
            self, text="Next", command=self.getrandom_2,
            style="GenerateButton.TButton",
            )
        generate_random.grid(column=2, row=2, sticky="EW")

        calculate_button = ttk.Button(
                self,
                text="Calculate",
                style="GenerateButton.TButton",
                command=self.calculate,

        )
        calculate_button.grid(column=1, row=2, sticky="EW")

        quit_button = ttk.Button(
            self,
            text="Quit",
            style="QuitButton.TButton",
            command=self.quit
            )
        quit_button.grid(column=4, row=2, sticky="EW")

        switch_page_button = ttk.Button(
            self,
            text="Add",
            style="GenerateButton.TButton",
            command=lambda: controller.show_frame(AddCalculation)
            )
        switch_page_button.grid(column=3, row=2, sticky="EW")

    def calculate(self, *args):

        a = self.a_value.get()
        b = self.b_value.get()
        c = a - b
        if c == self.answer_value.get():
            print(tk.messagebox.showinfo(title=(f"Answer ", {self.answer_value.get()}),
                                         message="You are correct"))
        else:
            print(tk.messagebox.showinfo(title=(f"Answer ", {self.answer_value.get()}),
                                         message="You are not correct"))

    def getrandom_2(self):
        self.a_value.set(random.randint(21, 50))
        self.b_value.set(random.randint(1, 20))




root = MathCalculation()

style = ttk.Style(root)
font.nametofont("TkDefaultFont").configure(size=14)
style.theme_use("clam")

style.configure("Background.TFrame", background=COLOUR_LIGHT_BACKGROUND, fill="both")

style.configure(
    "MyLabel.TLabel",
    background=COLOUR_LIGHT_BACKGROUND,
    foreground=COLOUR_LIGHT_TEXT,
)

style.configure("GenerateButton.TButton", borderwidth=0, background=COLOUR_BUTTON_NORMAL)
style.map(
    "GenerateButton.TButton",
    background=[("pressed", COLOUR_BUTTON_PRESSED), ("active", COLOUR_BUTTON_ACTIVE)],
)

style.configure("QuitButton.TButton", background=QUIT_BUTTON_NORMAL)
style.map(
    "QuitButton.TButton",
    background=[("pressed", QUIT_BUTTON_PRESSED), ("active", QUIT_BUTTON_ACTIVE)],
)


root.mainloop()
