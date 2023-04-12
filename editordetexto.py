import tkinter as tk
from tkinter import filedialog

class TextEditor:
    def __init__(self, master):
        self.master = master
        master.title("Editor de Texto")

        self.text_area = tk.Text(master, height=30, width=100)
        self.text_area.pack()

        self.save_button = tk.Button(master, text="Salvar", command=self.save_text)
        self.save_button.pack()

    def save_text(self):
        file_path = filedialog.asksaveasfilename(defaultextension='.txt')
        if file_path:
            with open(file_path, 'w') as file:
                file.write(self.text_area.get('1.0', 'end'))

root = tk.Tk()
text_editor = TextEditor(root)
root.mainloop()
