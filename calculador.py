import tkinter as tk

class Calculadora(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculadora")
        self.geometry("300x400")

        self.resultado_var = tk.StringVar()
        self.limpar_var = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        # Entry para exibir os resultados
        entry = tk.Entry(self, textvariable=self.resultado_var, font=('Arial', 24), bd=10, relief=tk.GROOVE, justify=tk.RIGHT)
        entry.grid(row=0, column=0, columnspan=4)

        # Botões
        botoes = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+',
            'C'  # Botão para limpar
        ]

        row_val = 1
        col_val = 0

        for botao in botoes:
            tk.Button(self, text=botao, padx=20, pady=20, font=('Arial', 18), bd=8, relief=tk.RIDGE, command=lambda b=botao: self.botao_click(b)).grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

    def botao_click(self, valor):
        if valor == '=':
            try:
                resultado = eval(self.resultado_var.get())
                self.resultado_var.set(resultado)
            except Exception as e:
                self.resultado_var.set("Erro")
        elif valor == 'C':
            self.resultado_var.set("")
        else:
            current_text = self.resultado_var.get()
            self.resultado_var.set(current_text + valor)


if __name__ == "__main__":
    app = Calculadora()
    app.mainloop()
