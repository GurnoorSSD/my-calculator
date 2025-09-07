import tkinter as tk

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Realistic Calculator")
        self.geometry("300x400")
        self.resizable(False, False)

        self.expression = ""

        # Display area
        self.display = tk.Entry(self, font=('Arial', 24), bd=10, relief=tk.RIDGE, justify='right')
        self.display.grid(row=0, column=0, columnspan=4, ipadx=10, ipady=10, sticky="nsew")

        # Create the buttons
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3),
        ]

        for (text, row, col) in buttons:
            tk.Button(self, text=text, font=('Arial', 18), command=lambda t=text: self.on_button_click(t)).grid(row=row, column=col, sticky="nsew", padx=2, pady=2)

        # Configure row/column resizing
        for i in range(5):
            self.grid_rowconfigure(i, weight=1)
        for j in range(4):
            self.grid_columnconfigure(j, weight=1)

        # Keyboard bindings
        self.bind("<Key>", self.on_key_press)

    def on_button_click(self, char):
        if char == "C":
            self.expression = ""
        elif char == "=":
            try:
                self.expression = str(eval(self.expression))
            except Exception:
                self.expression = "Error"
        else:
            self.expression += str(char)
        self.display.delete(0, tk.END)
        self.display.insert(0, self.expression)

    def on_key_press(self, event):
        key = event.char
        if key in "0123456789+-*/":
            self.expression += key
        elif key == "\r":  # Enter key
            try:
                self.expression = str(eval(self.expression))
            except Exception:
                self.expression = "Error"
        elif key == "\x08":  # Backspace
            self.expression = self.expression[:-1]
        self.display.delete(0, tk.END)
        self.display.insert(0, self.expression)

# Run the app
if __name__ == "__main__":
    calc = Calculator()
    calc.mainloop()
