import tkinter as tk

class Calculatrice:
    def __init__(self, master):
        self.master = master
        master.title("Calculatrice")

        self.equation = ""

        self.entry = tk.Entry(master, width=20, font=('Arial', 24), borderwidth=2, relief="solid", justify='right')
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('C', 5, 0), ('(', 5, 1), (')', 5, 2)
        ]

        for (text, row, col) in buttons:
            if text == '=':
                btn = tk.Button(master, text=text, width=5, height=2, font=('Arial', 18), command=self.evaluer)
            elif text == 'C':
                btn = tk.Button(master, text=text, width=5, height=2, font=('Arial', 18), command=self.clear)
            else:
                btn = tk.Button(master, text=text, width=5, height=2, font=('Arial', 18),
                                command=lambda txt=text: self.ajouter(txt))
            btn.grid(row=row, column=col, padx=5, pady=5)

    def ajouter(self, char):
        self.equation += str(char)
        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.equation)

    def evaluer(self):
        try:
            result = str(eval(self.equation))
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, result)
            self.equation = result
        except:
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, "Erreur")
            self.equation = ""

    def clear(self):
        self.equation = ""
        self.entry.delete(0, tk.END)

# Lancer l'application
root = tk.Tk()
app = Calculatrice(root)
root.mainloop()