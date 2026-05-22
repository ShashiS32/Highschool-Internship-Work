import tkinter as tk
from tkinter import font

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("400x500")
        self.root.resizable(False, False)
        
        self.expression = ""
        
        # Create display
        self.display_font = font.Font(family="Arial", size=20, weight="bold")
        self.display = tk.Entry(
            root,
            font=self.display_font,
            borderwidth=2,
            relief="solid",
            justify="right"
        )
        self.display.pack(fill="both", padx=10, pady=20, ipady=10)
        
        # Create button frame
        button_frame = tk.Frame(root)
        button_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Define button layout
        buttons = [
            ["C", "←", "/", "*"],
            ["7", "8", "9", "-"],
            ["4", "5", "6", "+"],
            ["1", "2", "3", "="],
            ["0", ".", ""]
        ]
        
        # Create buttons
        for row_idx, row in enumerate(buttons):
            for col_idx, button_text in enumerate(row):
                if button_text == "":
                    continue
                
                button = tk.Button(
                    button_frame,
                    text=button_text,
                    font=("Arial", 18, "bold"),
                    padx=20,
                    pady=20
                )
                
                # Bind commands
                if button_text == "C":
                    button.config(command=self.clear, bg="#ff6b6b", fg="white")
                elif button_text == "←":
                    button.config(command=self.backspace, bg="#ff6b6b", fg="white")
                elif button_text == "=":
                    button.config(command=self.calculate, bg="#51cf66", fg="white")
                elif button_text in ["+", "-", "*", "/"]:
                    button.config(command=lambda x=button_text: self.append_operator(x), bg="#4c6ef5", fg="white")
                else:
                    button.config(command=lambda x=button_text: self.append_number(x), bg="#e9ecef", fg="black")
                
                # Place button in grid
                if button_text == "0":
                    button.grid(row=row_idx, column=col_idx, columnspan=2, sticky="nsew", padx=5, pady=5)
                else:
                    button.grid(row=row_idx, column=col_idx, sticky="nsew", padx=5, pady=5)
        
        # Configure grid weights for resizing
        for i in range(5):
            button_frame.grid_rowconfigure(i, weight=1)
        for i in range(4):
            button_frame.grid_columnconfigure(i, weight=1)
    
    def append_number(self, number):
        self.expression += str(number)
        self.update_display()
    
    def append_operator(self, operator):
        if self.expression and self.expression[-1] not in "+-*/":
            self.expression += operator
            self.update_display()
    
    def calculate(self):
        try:
            result = eval(self.expression)
            self.expression = str(result)
            self.update_display()
        except:
            self.expression = ""
            self.display.delete(0, tk.END)
            self.display.insert(0, "Error")
    
    def clear(self):
        self.expression = ""
        self.update_display()
    
    def backspace(self):
        self.expression = self.expression[:-1]
        self.update_display()
    
    def update_display(self):
        self.display.delete(0, tk.END)
        self.display.insert(0, self.expression)

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
