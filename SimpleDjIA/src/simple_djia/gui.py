from __future__ import annotations

import tkinter as tk
from tkinter import filedialog, messagebox, ttk

from .library import load_library
from .profiles import SCENES, get_scene
from .session import create_session


class App(ttk.Frame):
    def __init__(self, root: tk.Tk) -> None:
        super().__init__(root, padding=16)
        self.root = root
        self.root.title("Simple DjIA")
        self.grid(sticky="nsew")
        self.columnconfigure(1, weight=1)
        self.library = tk.StringVar()
        self.scene = tk.StringVar(value="restaurant_piano")
        self.limit = tk.IntVar(value=12)
        self._build()

    def _build(self) -> None:
        ttk.Label(self, text="Simple DjIA", font=("TkDefaultFont", 20, "bold")).grid(row=0, column=0, columnspan=3, sticky="w")
        ttk.Label(self, text="Curadoria musical orientada por contexto humano, com critérios transparentes.").grid(row=1, column=0, columnspan=3, sticky="w", pady=(0, 14))
        ttk.Label(self, text="Biblioteca JSON").grid(row=2, column=0, sticky="w")
        ttk.Entry(self, textvariable=self.library).grid(row=2, column=1, sticky="ew", padx=8)
        ttk.Button(self, text="Abrir", command=self._choose).grid(row=2, column=2)
        ttk.Label(self, text="Comportamento").grid(row=3, column=0, sticky="w", pady=8)
        ttk.Combobox(self, textvariable=self.scene, values=tuple(SCENES), state="readonly").grid(row=3, column=1, columnspan=2, sticky="ew", padx=(8, 0))
        ttk.Label(self, text="Faixas").grid(row=4, column=0, sticky="w")
        ttk.Spinbox(self, from_=1, to=100, textvariable=self.limit).grid(row=4, column=1, columnspan=2, sticky="ew", padx=(8, 0))
        ttk.Button(self, text="Criar playlist humana", command=self._generate).grid(row=5, column=0, columnspan=3, sticky="ew", pady=12)
        self.output = tk.Text(self, height=20, width=80, wrap="word")
        self.output.grid(row=6, column=0, columnspan=3, sticky="nsew")
        self.rowconfigure(6, weight=1)

    def _choose(self) -> None:
        filename = filedialog.askopenfilename(filetypes=(("JSON", "*.json"), ("Todos", "*.*")))
        if filename:
            self.library.set(filename)

    def _generate(self) -> None:
        try:
            scene = get_scene(self.scene.get())
            session = create_session(load_library(self.library.get()), scene, self.limit.get())
        except Exception as exc:
            messagebox.showerror("Simple DjIA", str(exc))
            return
        self.output.delete("1.0", tk.END)
        self.output.insert(tk.END, f"{scene.name}\n{scene.description}\n\n")
        for i, ranked in enumerate(session.playlist, 1):
            t = ranked.track
            self.output.insert(tk.END, f"{i:02d}. {t.artist} — {t.title} | {t.bpm:g} BPM | {ranked.score:.2f}\n")


def main() -> None:
    root = tk.Tk()
    root.minsize(720, 560)
    App(root)
    root.mainloop()


if __name__ == "__main__":
    main()
