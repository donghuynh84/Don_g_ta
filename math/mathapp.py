import random
import tkinter as tk
import tkinter.font as font
from tkinter import messagebox
from tkinter import ttk

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
COLOUR_BUTTON_PRESSED = "#e797e8"

QUIT_BUTTON_NORMAL = "#4f79db"
QUIT_BUTTON_ACTIVE = "#2f7bf5"
QUIT_BUTTON_PRESSED = "#a81502"


class MathCalculation(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Math for Ava (c) by Don_g_ta")
        self.frames = dict()
        container = ttk.Frame(self, padding=(20, 10, 20, 0))
        container.grid(row=2, column=0, columnspan=2, sticky="EW")
        container.columnconfigure((0, 1, 2, 3), weight=0)

        for FrameClass in (AddCalculation, Substract, Mutiplication, Division):
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
        self.b_value = tk.IntVar(value=random.randint(1, 20))

        self.answer_value = tk.IntVar()
        first_label = ttk.Label(self, width=12, textvariable=self.a_value, style="MyLabel.TLabel")
        operator_label = ttk.Label(self, width=12, text="ADD", style="MyLabel.TLabel")
        second_label = ttk.Label(self, width=12, textvariable=self.b_value, style="MyLabel.TLabel")
        self.answer_input = ttk.Entry(self, width=12, textvariable=self.answer_value)
        first_label.grid(column=0, row=0,  sticky="W", padx=5)
        operator_label.grid(column=1, row=0,  sticky="W", padx=5)
        second_label.grid(column=2, row=0,  sticky="W", padx=5)
        self.answer_input.grid(column=3, row=0,  sticky="EW", padx=5)
        self.answer_input.delete(0, "end")
        self.answer_input.focus()

        generate_random = ttk.Button(
            self, text="Next",
            command=self.get_random,
            style="GenerateButton.TButton",
            cursor="heart"
        )
        generate_random.grid(column=0, row=2, sticky="W", padx=5)

        calculate_button = ttk.Button(
            self,
            text="Calculate",
            command=self.calculate,
            style="GenerateButton.TButton",
            cursor="heart"

        )
        calculate_button.grid(column=1, row=2, sticky="W", padx=5)

        clear_button = ttk.Button(
            self,
            text="Clear",
            command=self.clear_text,
            style="GenerateButton.TButton",
            cursor="heart"
        )

        clear_button.grid(row=2, column=2, sticky="W", padx=5)

        quit_button = ttk.Button(
            self,
            text="Quit",
            command=self.quit,
            style="QuitButton.TButton",
            cursor="heart"
        )
        quit_button.grid(column=3, row=2, sticky="W", padx=5)

        switch_page_button = ttk.Button(
            self,
            text="Substract",
            style="GenerateButton.TButton",
            command=lambda: controller.show_frame(Substract),
            cursor="heart"
        )

        switch_page_button.grid(row=3, column=0, sticky="W", padx=5)

        switch_page_button = ttk.Button(
            self,
            text="Multiply",
            style="GenerateButton.TButton",
            command=lambda: controller.show_frame(Mutiplication),
            cursor="heart"
        )

        switch_page_button.grid(row=3, column=1, sticky="W", padx=5)

        switch_page_button = ttk.Button(
            self,
            text="Division",
            style="GenerateButton.TButton",
            command=lambda: controller.show_frame(Division),
            cursor="heart"
    )

        switch_page_button.grid(row=3, column=2, sticky="W", padx=5)

    def calculate(self, *args):

        a = self.a_value.get()
        b = self.b_value.get()
        c = a + b
        if c == self.answer_value.get():
            print(tk.messagebox.showinfo(title=(f"Answer", {self.answer_value.get()}),
                                         message="You are correct"))
            self.clear_text()
            self.get_random()
        else:
            print(tk.messagebox.showinfo(title=(f"Answer ", {self.answer_value.get()}),
                                         message="You are not correct"))
            self.clear_text()
            self.get_random()

    def get_random(self):
        self.a_value.set(random.randint(1, 50))
        self.b_value.set(random.randint(1, 20))
        self.answer_input.delete(0, 'end')
        self.answer_input.focus()

    def clear_text(self):
        self.answer_input.delete(0, 'end')
        self.answer_input.focus()


class Substract(ttk.Frame):
    def __init__(self, container, controller):
        super().__init__(container)

        self.a_value = tk.IntVar(value=random.randint(21, 51))
        self.b_value = tk.IntVar(value=random.randint(1, 20))

        self.answer_value = tk.IntVar()
        first_label = ttk.Label(self, width=12, textvariable=self.a_value, style="MyLabel.TLabel")
        operator_label = ttk.Label(self, width=12, text="MINUS", style="MyLabel.TLabel")
        second_label = ttk.Label(self, width=12, textvariable=self.b_value, style="MyLabel.TLabel")
        self.answer_input = ttk.Entry(self, width=12, textvariable=self.answer_value)
        first_label.grid(column=0, row=0,  sticky="W", padx=5)
        operator_label.grid(column=1, row=0,  sticky="W", padx=5)
        second_label.grid(column=2, row=0,  sticky="W", padx=5)
        self.answer_input.grid(column=3, row=0, sticky="EW", padx=5)
        self.answer_input.delete(0, "end")
        self.answer_input.focus()

        generate_random = ttk.Button(
            self, text="Next",
            command=self.get_random_2,
            style="GenerateButton.TButton",
            cursor="heart"
        )
        generate_random.grid(column=0, row=2, sticky="W", padx=5)

        calculate_button = ttk.Button(
            self,
            text="Calculate",
            command=self.calculate,
            style="GenerateButton.TButton",
            cursor="heart"


        )
        calculate_button.grid(column=1, row=2, sticky="W", padx=5)

        clear_button = ttk.Button(
            self,
            text="Clear",
            command=self.clear_text,
            style="GenerateButton.TButton",
            cursor="heart"
        )

        clear_button.grid(row=2, column=2, sticky="W", padx=5)

        quit_button = ttk.Button(
            self,
            text="Quit",
            command=self.quit,
            style="QuitButton.TButton",
            cursor="heart"
        )
        quit_button.grid(column=3, row=2, sticky="W", padx=5)

        switch_page_button = ttk.Button(
            self,
            text="Add",
            style="GenerateButton.TButton",
            cursor="heart",
            command=lambda: controller.show_frame(AddCalculation)
            )
        switch_page_button.grid(row=3, column=0, sticky="EW", padx=5)

        switch_page_button = ttk.Button(
            self,
            text="Multiply",
            style="GenerateButton.TButton",
            cursor="heart",
            command=lambda: controller.show_frame(Mutiplication)
            )
        switch_page_button.grid(row=3, column=1, sticky="EW", padx=5)

        switch_page_button = ttk.Button(
            self,
            text="Division",
            style="GenerateButton.TButton",
            cursor="heart",
            command=lambda: controller.show_frame(Division)
            )
        switch_page_button.grid(row=3, column=2, sticky="EW", padx=5)

    def calculate(self, *args):

        a = self.a_value.get()
        b = self.b_value.get()
        c = a - b
        if c == self.answer_value.get():
            print(tk.messagebox.showinfo(title=(f"Answer ", {self.answer_value.get()}),
                                         message="You are correct"))
            self.clear_text()
            self.get_random_2()
        else:
            print(tk.messagebox.showinfo(title=(f"Answer ", {self.answer_value.get()}),
                                         message="You are not correct"))
            self.clear_text()
            self.get_random_2()

    def get_random_2(self):

        self.a_value.set(random.randint(21, 50))
        self.b_value.set(random.randint(1, 20))
        self.answer_input.delete(0, 'end')
        self.answer_input.focus()

    def clear_text(self):
        self.answer_input.delete(0, 'end')
        self.answer_input.focus()

# doing the multiplication


class Mutiplication(ttk.Frame):
    def __init__(self, container, controller):
        super().__init__(container)

        self.a_value = tk.IntVar(value=random.randint(1, 12))
        self.b_value = tk.IntVar(value=random.randint(1, 12))

        self.answer_value = tk.IntVar()
        first_label = ttk.Label(self, width=12, textvariable=self.a_value, style="MyLabel.TLabel")
        operator_label = ttk.Label(self, width=12, text="TIMES", style="MyLabel.TLabel")
        second_label = ttk.Label(self, width=12, textvariable=self.b_value, style="MyLabel.TLabel")
        self.answer_input = ttk.Entry(self, width=12, textvariable=self.answer_value)
        first_label.grid(column=0, row=0,  sticky="W", padx=5)
        operator_label.grid(column=1, row=0,  sticky="W", padx=5)
        second_label.grid(column=2, row=0,  sticky="W", padx=5)
        self.answer_input.grid(column=3, row=0,  sticky="EW", padx=5)
        self.answer_input.delete(0, "end")
        self.answer_input.focus()

        generate_random = ttk.Button(
            self,
            text="Next",
            command=self.get_random_3,
            style="GenerateButton.TButton",
            cursor="heart"
        )
        generate_random.grid(column=0, row=2, sticky="W", padx=5)

        calculate_button = ttk.Button(
            self,
            text="Calculate",
            command=self.calculate,
            style="GenerateButton.TButton",
            cursor="heart"


        )
        calculate_button.grid(column=1, row=2, sticky="W", padx=5)

        clear_button = ttk.Button(
            self,
            text="Clear",
            command= self.clear_text,
            style="GenerateButton.TButton",
            cursor="heart"
        )

        clear_button.grid(row=2, column=2, sticky="W", padx=5)

        quit_button = ttk.Button(
            self,
            text="Quit",
            command=self.quit,
            style="QuitButton.TButton",
            cursor="heart"
        )
        quit_button.grid(column=3, row=2, sticky="W", padx=5)

        switch_page_button = ttk.Button(
            self,
            text="Add",
            style="GenerateButton.TButton",
            cursor="heart",
            command=lambda: controller.show_frame(AddCalculation)
            )
        switch_page_button.grid(row=3, column=0, sticky="EW", padx=5)

        switch_page_button = ttk.Button(
            self,
            text="Substract",
            style="GenerateButton.TButton",
            cursor="heart",
            command=lambda: controller.show_frame(Substract)
            )
        switch_page_button.grid(row=3, column=1, sticky="EW", padx=5)

        switch_page_button = ttk.Button(
            self,
            text="Division",
            style="GenerateButton.TButton",
            cursor="heart",
            command=lambda: controller.show_frame(Division)
            )
        switch_page_button.grid(row=3, column=2, sticky="EW", padx=5)

    def calculate(self, *args):

        a = self.a_value.get()
        b = self.b_value.get()
        c = a * b

        if c == self.answer_value.get():
            print(tk.messagebox.showinfo(title=(f"Answer ", {self.answer_value.get()}),
                                         message="You are correct"))
            self.clear_text()
            self.get_random_3()

        else:
            print(tk.messagebox.showinfo(title=(f"Answer ", {self.answer_value.get()}),
                                         message="You are not correct"))
            self.clear_text()
            self.get_random_3()

    def get_random_3(self):
        self.a_value.set(random.randint(1, 12))
        self.b_value.set(random.randint(1, 12))
        self.answer_input.delete(0, 'end')

    def clear_text(self):
        self.answer_input.delete(0, 'end')
        self.answer_input.focus()


class Division(ttk.Frame):
    def __init__(self, container, controller):
        super().__init__(container)

        self.a_value = tk.IntVar(value=10)
        self.b_value = tk.IntVar(value=2)
        self.answer_value = tk.IntVar()
        first_label = ttk.Label(self, width=12, textvariable=self.a_value, style="MyLabel.TLabel")
        operator_label = ttk.Label(self, width=12, text="DIVIDE", style="MyLabel.TLabel")
        second_label = ttk.Label(self, width=12, textvariable=self.b_value, style="MyLabel.TLabel")
        self.answer_input = ttk.Entry(self, width=12, textvariable=self.answer_value)
        first_label.grid(column=0, row=0,  sticky="W", padx=5)
        operator_label.grid(column=1, row=0,  sticky="W", padx=5)
        second_label.grid(column=2, row=0,  sticky="W", padx=5)
        self.answer_input.grid(column=3, row=0,  sticky="EW", padx=5)
        self.answer_input.delete(0, "end")
        self.answer_input.focus()

        generate_random = ttk.Button(
            self, text="Next",
            command=self.get_random_4,
            style="GenerateButton.TButton",
            cursor="heart"
        )
        generate_random.grid(column=0, row=2, sticky="W", padx=5)

        calculate_button = ttk.Button(
            self,
            text="Calculate",
            command=self.calculate,
            style="GenerateButton.TButton",
            cursor="heart"

        )
        calculate_button.grid(column=1, row=2, sticky="W", padx=5)

        clear_button = ttk.Button(
            self,
            text="Clear",
            command=self.clear_text,
            style="GenerateButton.TButton",
            cursor="heart"
        )

        clear_button.grid(row=2, column=2, sticky="W", padx=5)

        quit_button = ttk.Button(
            self,
            text="Quit",
            command=self.quit,
            style="QuitButton.TButton",
            cursor="heart"
        )
        quit_button.grid(column=3, row=2, sticky="W", padx=5)

        switch_page_button = ttk.Button(
            self,
            text="Substract",
            style="GenerateButton.TButton",
            command=lambda: controller.show_frame(Substract),
            cursor="heart"
        )

        switch_page_button.grid(row=3, column=0, sticky="W", padx=5)

        switch_page_button = ttk.Button(
            self,
            text="Multiply",
            style="GenerateButton.TButton",
            command=lambda: controller.show_frame(Mutiplication),
            cursor="heart"
        )

        switch_page_button.grid(row=3, column=1, sticky="W", padx=5)

        switch_page_button = ttk.Button(
            self,
            text="Add",
            style="GenerateButton.TButton",
            command=lambda: controller.show_frame(AddCalculation),
            cursor="heart"
        )

        switch_page_button.grid(row=3, column=2, sticky="W", padx=5)

    def calculate(self, *args):
        a = self.a_value.get()
        b = self.b_value.get()
        c = a / b
        if c == self.answer_value.get():
            print(tk.messagebox.showinfo(title=(f"Answer", {self.answer_value.get()}),
                                             message="You are correct"))
            self.clear_text()
            self.get_random_4()
        else:
            print(tk.messagebox.showinfo(title=(f"Answer ", {self.answer_value.get()}),
                                             message="You are not correct"))
            self.clear_text()
            self.get_random_4()

    def get_random_4(self):
        self.b_value.set(random.randint(1, 12))
        self.a_value.set(self.b_value.get() * random.randint(1, 12))
        self.answer_input.delete(0, 'end')
        self.answer_input.focus()

    def clear_text(self):
        self.answer_input.delete(0, 'end')
        self.answer_input.focus()


root = MathCalculation()

style = ttk.Style(root)
font.nametofont("TkDefaultFont").configure(size=14)
style.theme_use("alt")

style.configure("Background.TFrame", background=COLOUR_LIGHT_BACKGROUND, fill="both")

style.configure(
    "MyLabel.TLabel",
    background=COLOUR_LIGHT_BACKGROUND,
    foreground=COLOUR_LIGHT_TEXT,
)

style.configure("GenerateButton.TButton", background=COLOUR_BUTTON_NORMAL)
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