from __future__ import annotations

import subprocess
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

from .library import load_library
from .player import detect_backend, play
from .profiles import SCENES, get_scene
from .session import Session, create_session


class App(ttk.Frame):
    def __init__(self, root: tk.Tk) -> None:
        super().__init__(root, padding=16)
        self.root = root
        self.root.title("Simple DjIA")
        self.grid(sticky="nsew")
        self.columnconfigure(1, weight=1)
        self.rowconfigure(7, weight=1)
        self.library = tk.StringVar()
        self.scene = tk.StringVar(value="restaurant_piano")
        self.limit = tk.IntVar(value=12)
        self.status = tk.StringVar(value="Escolha uma biblioteca e um comportamento.")
        self.session: Session | None = None
        self.process: subprocess.Popen | None = None
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

        controls = ttk.Frame(self)
        controls.grid(row=6, column=0, columnspan=3, sticky="ew", pady=(0, 8))
        for column in range(3):
            controls.columnconfigure(column, weight=1)
        ttk.Button(controls, text="Reproduzir selecionada", command=self._play_selected).grid(row=0, column=0, sticky="ew", padx=(0, 4))
        ttk.Button(controls, text="Próxima", command=self._play_next).grid(row=0, column=1, sticky="ew", padx=4)
        ttk.Button(controls, text="Parar", command=self._stop).grid(row=0, column=2, sticky="ew", padx=(4, 0))

        self.playlist = ttk.Treeview(self, columns=("artist", "title", "bpm", "score", "why"), show="headings", height=18)
        for key, label, width in (
            ("artist", "Artista", 140), ("title", "Música", 220), ("bpm", "BPM", 60),
            ("score", "Aderência", 75), ("why", "Critérios humanos", 330),
        ):
            self.playlist.heading(key, text=label)
            self.playlist.column(key, width=width, anchor="w")
        self.playlist.grid(row=7, column=0, columnspan=3, sticky="nsew")
        ttk.Label(self, textvariable=self.status).grid(row=8, column=0, columnspan=3, sticky="w", pady=(8, 0))
        self.root.protocol("WM_DELETE_WINDOW", self._close)

    def _choose(self) -> None:
        filename = filedialog.askopenfilename(filetypes=(("JSON", "*.json"), ("Todos", "*.*")))
        if filename:
            self.library.set(filename)

    def _generate(self) -> None:
        try:
            scene = get_scene(self.scene.get())
            self.session = create_session(load_library(self.library.get()), scene, self.limit.get())
        except Exception as exc:
            messagebox.showerror("Simple DjIA", str(exc))
            return
        for item in self.playlist.get_children():
            self.playlist.delete(item)
        for index, ranked in enumerate(self.session.playlist):
            t = ranked.track
            why = "; ".join(ranked.reasons[:4]) or "equilíbrio geral do perfil"
            self.playlist.insert("", "end", iid=str(index), values=(t.artist, t.title, f"{t.bpm:g}", f"{ranked.score:.2f}", why))
        if self.session.playlist:
            self.playlist.selection_set("0")
            self.status.set(f"{scene.name}: {len(self.session.playlist)} faixas organizadas.")
        else:
            self.status.set("Nenhuma faixa compatível com o comportamento escolhido.")

    def _selected_index(self) -> int | None:
        selected = self.playlist.selection()
        if not selected:
            return None
        return int(selected[0])

    def _play_index(self, index: int) -> None:
        if self.session is None or not 0 <= index < len(self.session.playlist):
            return
        backend = detect_backend()
        if backend is None:
            messagebox.showerror("Simple DjIA", "Nenhum player aberto encontrado. Instale mpv, VLC/cvlc ou ffplay.")
            return
        self._stop()
        ranked = self.session.playlist[index]
        try:
            self.process = play(ranked.track.path, backend)
        except (OSError, RuntimeError) as exc:
            messagebox.showerror("Simple DjIA", str(exc))
            return
        self.session.current_index = index
        self.playlist.selection_set(str(index))
        self.playlist.see(str(index))
        self.status.set(f"Tocando: {ranked.track.artist} — {ranked.track.title} via {backend.name}")

    def _play_selected(self) -> None:
        index = self._selected_index()
        if index is not None:
            self._play_index(index)

    def _play_next(self) -> None:
        if self.session is None or not self.session.playlist:
            return
        index = min(self.session.current_index + 1, len(self.session.playlist) - 1)
        self._play_index(index)

    def _stop(self) -> None:
        if self.process is not None and self.process.poll() is None:
            self.process.terminate()
            try:
                self.process.wait(timeout=2)
            except subprocess.TimeoutExpired:
                self.process.kill()
        self.process = None

    def _close(self) -> None:
        self._stop()
        self.root.destroy()


def main() -> None:
    root = tk.Tk()
    root.minsize(980, 620)
    App(root)
    root.mainloop()


if __name__ == "__main__":
    main()
