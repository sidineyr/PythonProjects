import tkinter as tk
from tkinter import messagebox
import subprocess

# Função de callback para o botão formatar
def formatar_pendrive():
    # Obtém o dispositivo selecionado na lista
    dispositivo = device_listbox.get(tk.ACTIVE)
    # Comando para formatar o pendrive em EXT4
    comando = f"sudo mkfs.ext4 {dispositivo}"
    # Executa o comando no terminal
    subprocess.call(comando, shell=True)
    messagebox.showinfo("Formatar Pendrive", f"Pendrive {dispositivo} formatado em EXT4!")

# Função de callback para o botão fechar
def fechar_aplicativo():
    root.destroy()

# Cria a janela principal
root = tk.Tk()
root.title("Pendrive Status")

# Obtém a lista de dispositivos conectados
comando = "lsblk -o NAME,MOUNTPOINT | grep /media | awk '{print $1}'"
dispositivos = subprocess.check_output(comando, shell=True).decode().split()

# Cria a lista de dispositivos
device_listbox = tk.Listbox(root)
for dispositivo in dispositivos:
    device_listbox.insert(tk.END, dispositivo)
device_listbox.pack(pady=10)

# Cria o botão de formatação
format_button = tk.Button(root, text="Formatar Pendrive em EXT4", command=formatar_pendrive)
format_button.pack(pady=10)

# Cria o botão de fechar
close_button = tk.Button(root, text="Fechar", command=fechar_aplicativo)
close_button.pack(pady=10)

root.mainloop()
