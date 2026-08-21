"""Tkinter desktop interface for Python Music Composer."""

from __future__ import annotations

import os
from pathlib import Path
import subprocess
import sys
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

from .composer import compose_melody
from .harmony import PROGRESSIONS, build_accompaniment
from .midi import write_midi

ROOT_NOTES = ("C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B")
SCALES = {"Maior": "major", "Menor natural": "minor"}
TIME_SIGNATURES = {"4/4": 4, "3/4": 3, "2/4": 2}
INSTRUMENTS = {
    "Piano": 0, "Piano elétrico": 4, "Violão": 24, "Guitarra limpa": 27,
    "Baixo acústico": 32, "Violino": 40, "Violoncelo": 42, "Cordas": 48,
    "Trompete": 56, "Sax alto": 65, "Flauta": 73, "Sintetizador": 80,
}


class MusicComposerApp(ttk.Frame):
    def __init__(self, master: tk.Tk) -> None:
        super().__init__(master, padding=18)
        self.master = master
        self.last_output: Path | None = None
        self.master.title("Python Music Composer")
        self.master.minsize(650, 650)
        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)
        self.grid(sticky="nsew")
        self.columnconfigure(1, weight=1)
        self._build_variables()
        self._build_layout()

    def _build_variables(self) -> None:
        self.root_note = tk.StringVar(value="C")
        self.scale_name = tk.StringVar(value="Maior")
        self.octave = tk.IntVar(value=4)
        self.bars = tk.IntVar(value=8)
        self.time_signature = tk.StringVar(value="4/4")
        self.tempo = tk.IntVar(value=100)
        self.instrument = tk.StringVar(value="Piano")
        self.progression = tk.StringVar(value="I-V-vi-IV")
        self.harmony_enabled = tk.BooleanVar(value=True)
        self.randomness = tk.IntVar(value=45)
        self.seed = tk.StringVar(value="")
        self.output = tk.StringVar(value="composition.mid")
        self.status = tk.StringVar(value="Pronto para compor.")

    def _build_layout(self) -> None:
        ttk.Label(self, text="Python Music Composer", font=("TkDefaultFont", 18, "bold")).grid(row=0, column=0, columnspan=3, sticky="w")
        ttk.Label(self, text="Melodia, harmonia e baixo construídos a partir da teoria musical.").grid(row=1, column=0, columnspan=3, sticky="w", pady=(4, 16))
        self._combo(2, "Tonalidade", self.root_note, ROOT_NOTES)
        self._combo(3, "Escala", self.scale_name, tuple(SCALES))
        self._spin(4, "Oitava da melodia", self.octave, 1, 7)
        self._spin(5, "Compassos", self.bars, 1, 64)
        self._combo(6, "Compasso", self.time_signature, tuple(TIME_SIGNATURES))
        self._spin(7, "BPM", self.tempo, 40, 240)
        self._combo(8, "Instrumento melódico", self.instrument, tuple(INSTRUMENTS))
        self._combo(9, "Progressão harmônica", self.progression, tuple(PROGRESSIONS))
        ttk.Checkbutton(self, text="Adicionar acordes e linha de baixo", variable=self.harmony_enabled).grid(row=10, column=0, columnspan=3, sticky="w", pady=6)

        ttk.Label(self, text="Aleatoriedade").grid(row=11, column=0, sticky="w", pady=6)
        ttk.Scale(self, from_=0, to=100, variable=self.randomness, command=self._update_randomness).grid(row=11, column=1, sticky="ew", padx=(10, 8))
        self.randomness_label = ttk.Label(self, text="45%", width=5)
        self.randomness_label.grid(row=11, column=2, sticky="w")
        ttk.Label(self, text="Seed (opcional)").grid(row=12, column=0, sticky="w", pady=6)
        ttk.Entry(self, textvariable=self.seed).grid(row=12, column=1, columnspan=2, sticky="ew", padx=(10, 0))
        ttk.Label(self, text="Arquivo MIDI").grid(row=13, column=0, sticky="w", pady=6)
        ttk.Entry(self, textvariable=self.output).grid(row=13, column=1, sticky="ew", padx=(10, 8))
        ttk.Button(self, text="Escolher...", command=self.choose_output).grid(row=13, column=2, sticky="ew")

        controls = ttk.Frame(self)
        controls.grid(row=14, column=0, columnspan=3, sticky="ew", pady=(20, 10))
        controls.columnconfigure((0, 1), weight=1)
        ttk.Button(controls, text="Gerar música", command=self.generate).grid(row=0, column=0, sticky="ew", padx=(0, 6))
        self.open_button = ttk.Button(controls, text="Abrir MIDI", command=self.open_last_output, state="disabled")
        self.open_button.grid(row=0, column=1, sticky="ew", padx=(6, 0))
        ttk.Separator(self).grid(row=15, column=0, columnspan=3, sticky="ew", pady=(4, 10))
        ttk.Label(self, textvariable=self.status).grid(row=16, column=0, columnspan=3, sticky="w")

    def _combo(self, row, label, variable, values) -> None:
        ttk.Label(self, text=label).grid(row=row, column=0, sticky="w", pady=6)
        ttk.Combobox(self, textvariable=variable, values=values, state="readonly").grid(row=row, column=1, columnspan=2, sticky="ew", padx=(10, 0))

    def _spin(self, row, label, variable, minimum, maximum) -> None:
        ttk.Label(self, text=label).grid(row=row, column=0, sticky="w", pady=6)
        ttk.Spinbox(self, textvariable=variable, from_=minimum, to=maximum).grid(row=row, column=1, columnspan=2, sticky="ew", padx=(10, 0))

    def _update_randomness(self, _value: str) -> None:
        self.randomness_label.configure(text=f"{self.randomness.get()}%")

    def choose_output(self) -> None:
        filename = filedialog.asksaveasfilename(title="Salvar composição MIDI", defaultextension=".mid", filetypes=(("MIDI", "*.mid"), ("Todos", "*.*")))
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
            beats = TIME_SIGNATURES[self.time_signature.get()]
            progression = self.progression.get()
            melody = compose_melody(
                root=self.root_note.get(), scale=SCALES[self.scale_name.get()], octave=self.octave.get(),
                bars=self.bars.get(), beats_per_bar=beats, randomness=self.randomness.get() / 100,
                seed=self._seed_value(), progression=progression,
            )
            chords, bass = ([], [])
            if self.harmony_enabled.get():
                chords, bass = build_accompaniment(self.root_note.get(), SCALES[self.scale_name.get()], self.bars.get(), beats, progression)
            output = Path(self.output.get().strip() or "composition.mid")
            if output.suffix.lower() not in {".mid", ".midi"}:
                output = output.with_suffix(".mid")
                self.output.set(str(output))
            path = write_midi(melody, output, self.tempo.get(), INSTRUMENTS[self.instrument.get()], chords, bass, beats)
        except (OSError, ValueError, KeyError, tk.TclError) as exc:
            messagebox.showerror("Não foi possível gerar a música", str(exc))
            self.status.set("Erro ao gerar composição.")
            return
        self.last_output = path.resolve()
        self.open_button.configure(state="normal")
        self.status.set(f"Criado: {self.last_output} — {len(melody)} notas, {len(chords)} acordes")
        messagebox.showinfo("Composição concluída", f"MIDI criado:\n{self.last_output}")

    def open_last_output(self) -> None:
        if not self.last_output or not self.last_output.exists():
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
