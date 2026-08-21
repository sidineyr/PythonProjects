"""Tkinter desktop interface for Python Music Composer."""

from __future__ import annotations

import os
from pathlib import Path
import subprocess
import sys
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

from .composer import compose_melody
from .midi import write_midi

ROOT_NOTES = ("C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B")
SCALES = {"Maior": "major", "Menor natural": "minor"}
TIME_SIGNATURES = {"4/4": 4, "3/4": 3, "2/4": 2}
INSTRUMENTS = {
    "Piano": 0,
    "Piano elétrico": 4,
    "Violão": 24,
    "Guitarra limpa": 27,
    "Baixo acústico": 32,
    "Violino": 40,
    "Violoncelo": 42,
    "Cordas": 48,
    "Trompete": 56,
    "Sax alto": 65,
    "Flauta": 73,
    "Sintetizador": 80,
}


class MusicComposerApp(ttk.Frame):
    """Desktop UI backed by the scale-aware composition engine."""

    def __init__(self, master: tk.Tk) -> None:
        super().__init__(master, padding=18)
        self.master = master
        self.last_output: Path | None = None
        self._configure_window()
        self._build_variables()
        self._build_layout()

    def _configure_window(self) -> None:
        self.master.title("Python Music Composer")
        self.master.minsize(620, 540)
        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)
        self.grid(sticky="nsew")
        self.columnconfigure(1, weight=1)

    def _build_variables(self) -> None:
        self.root_note = tk.StringVar(value="C")
        self.scale_name = tk.StringVar(value="Maior")
        self.octave = tk.IntVar(value=4)
        self.bars = tk.IntVar(value=8)
        self.time_signature = tk.StringVar(value="4/4")
        self.tempo = tk.IntVar(value=100)
        self.instrument = tk.StringVar(value="Piano")
        self.randomness = tk.IntVar(value=55)
        self.seed = tk.StringVar(value="")
        self.output = tk.StringVar(value="composition.mid")
        self.status = tk.StringVar(value="Pronto para compor.")

    def _build_layout(self) -> None:
        title = ttk.Label(self, text="Python Music Composer", font=("TkDefaultFont", 18, "bold"))
        title.grid(row=0, column=0, columnspan=3, sticky="w", pady=(0, 4))
        ttk.Label(
            self,
            text="Crie melodias MIDI coerentes com tonalidade, escala, andamento e instrumento.",
        ).grid(row=1, column=0, columnspan=3, sticky="w", pady=(0, 18))

        self._combo_row(2, "Tonalidade", self.root_note, ROOT_NOTES)
        self._combo_row(3, "Escala", self.scale_name, tuple(SCALES))
        self._spin_row(4, "Oitava", self.octave, 1, 7)
        self._spin_row(5, "Compassos", self.bars, 1, 64)
        self._combo_row(6, "Compasso", self.time_signature, tuple(TIME_SIGNATURES))
        self._spin_row(7, "BPM", self.tempo, 40, 240)
        self._combo_row(8, "Instrumento", self.instrument, tuple(INSTRUMENTS))

        ttk.Label(self, text="Aleatoriedade").grid(row=9, column=0, sticky="w", pady=6)
        randomness = ttk.Scale(
            self,
            from_=0,
            to=100,
            variable=self.randomness,
            command=self._update_randomness_label,
        )
        randomness.grid(row=9, column=1, sticky="ew", padx=(10, 8), pady=6)
        self.randomness_label = ttk.Label(self, text="55%", width=5)
        self.randomness_label.grid(row=9, column=2, sticky="w")

        ttk.Label(self, text="Seed (opcional)").grid(row=10, column=0, sticky="w", pady=6)
        ttk.Entry(self, textvariable=self.seed).grid(row=10, column=1, columnspan=2, sticky="ew", padx=(10, 0), pady=6)

        ttk.Label(self, text="Arquivo MIDI").grid(row=11, column=0, sticky="w", pady=6)
        ttk.Entry(self, textvariable=self.output).grid(row=11, column=1, sticky="ew", padx=(10, 8), pady=6)
        ttk.Button(self, text="Escolher...", command=self.choose_output).grid(row=11, column=2, sticky="ew", pady=6)

        controls = ttk.Frame(self)
        controls.grid(row=12, column=0, columnspan=3, sticky="ew", pady=(20, 10))
        controls.columnconfigure(0, weight=1)
        controls.columnconfigure(1, weight=1)
        ttk.Button(controls, text="Gerar música", command=self.generate).grid(row=0, column=0, sticky="ew", padx=(0, 6))
        self.open_button = ttk.Button(controls, text="Abrir MIDI", command=self.open_last_output, state="disabled")
        self.open_button.grid(row=0, column=1, sticky="ew", padx=(6, 0))

        ttk.Separator(self).grid(row=13, column=0, columnspan=3, sticky="ew", pady=(4, 10))
        ttk.Label(self, textvariable=self.status).grid(row=14, column=0, columnspan=3, sticky="w")

    def _combo_row(self, row: int, label: str, variable: tk.Variable, values: tuple[str, ...]) -> None:
        ttk.Label(self, text=label).grid(row=row, column=0, sticky="w", pady=6)
        combo = ttk.Combobox(self, textvariable=variable, values=values, state="readonly")
        combo.grid(row=row, column=1, columnspan=2, sticky="ew", padx=(10, 0), pady=6)

    def _spin_row(self, row: int, label: str, variable: tk.Variable, minimum: int, maximum: int) -> None:
        ttk.Label(self, text=label).grid(row=row, column=0, sticky="w", pady=6)
        ttk.Spinbox(self, textvariable=variable, from_=minimum, to=maximum).grid(
            row=row, column=1, columnspan=2, sticky="ew", padx=(10, 0), pady=6
        )

    def _update_randomness_label(self, _value: str) -> None:
        self.randomness_label.configure(text=f"{self.randomness.get()}%")

    def choose_output(self) -> None:
        filename = filedialog.asksaveasfilename(
            title="Salvar composição MIDI",
            defaultextension=".mid",
            filetypes=(("MIDI", "*.mid"), ("Todos os arquivos", "*.*")),
            initialfile=Path(self.output.get()).name or "composition.mid",
        )
        if filename:
            self.output.set(filename)

    def _seed_value(self) -> int | None:
        raw = self.seed.get().strip()
        if not raw:
            return None
        try:
            return int(raw)
        except ValueError as exc:
            raise ValueError("A seed deve ser um número inteiro.") from exc

    def generate(self) -> None:
        try:
            output = Path(self.output.get().strip() or "composition.mid")
            if output.suffix.lower() not in {".mid", ".midi"}:
                output = output.with_suffix(".mid")
                self.output.set(str(output))

            melody = compose_melody(
                root=self.root_note.get(),
                scale=SCALES[self.scale_name.get()],
                octave=self.octave.get(),
                bars=self.bars.get(),
                beats_per_bar=TIME_SIGNATURES[self.time_signature.get()],
                randomness=self.randomness.get() / 100.0,
                seed=self._seed_value(),
            )
            path = write_midi(
                melody,
                output,
                tempo=self.tempo.get(),
                instrument=INSTRUMENTS[self.instrument.get()],
            )
        except (OSError, ValueError, KeyError, tk.TclError) as exc:
            messagebox.showerror("Não foi possível gerar a música", str(exc))
            self.status.set("Erro ao gerar composição.")
            return

        self.last_output = path.resolve()
        self.open_button.configure(state="normal")
        self.status.set(f"Criado: {self.last_output} — {len(melody)} notas")
        messagebox.showinfo("Composição concluída", f"Arquivo MIDI criado com sucesso:\n{self.last_output}")

    def open_last_output(self) -> None:
        if not self.last_output or not self.last_output.exists():
            messagebox.showwarning("Arquivo indisponível", "Gere uma composição primeiro.")
            return
        try:
            if sys.platform.startswith("win"):
                os.startfile(self.last_output)  # type: ignore[attr-defined]
            elif sys.platform == "darwin":
                subprocess.run(["open", str(self.last_output)], check=True)
            else:
                subprocess.run(["xdg-open", str(self.last_output)], check=True)
        except (OSError, subprocess.CalledProcessError) as exc:
            messagebox.showerror("Não foi possível abrir o MIDI", str(exc))


def run_gui() -> None:
    root = tk.Tk()
    MusicComposerApp(root)
    root.mainloop()
