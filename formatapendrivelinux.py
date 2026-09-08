"""Interface Linux para formatar, com confirmação, uma partição USB removível."""

from __future__ import annotations

import json
import os
from pathlib import Path
import shutil
import subprocess
import tkinter as tk
from tkinter import messagebox, simpledialog
from typing import Any


def _esta_montado(valor: Any) -> bool:
    if isinstance(valor, list):
        return any(item for item in valor)
    return bool(valor)


def extrair_particoes_seguras(dados: dict[str, Any]) -> list[dict[str, str]]:
    """Retorna apenas partições removíveis, graváveis e desmontadas."""
    candidatas: list[dict[str, str]] = []

    def visitar(
        item: dict[str, Any],
        removivel_pai: bool = False,
        modelo_pai: str = "",
    ) -> None:
        removivel = bool(item.get("rm")) or removivel_pai
        modelo = str(item.get("model") or modelo_pai).strip()
        caminho = str(item.get("path") or "")
        montagens = item.get("mountpoints", item.get("mountpoint"))

        if (
            item.get("type") == "part"
            and removivel
            and not bool(item.get("ro"))
            and not _esta_montado(montagens)
            and caminho.startswith("/dev/")
            and Path(caminho).name == caminho.removeprefix("/dev/")
        ):
            candidatas.append(
                {
                    "path": caminho,
                    "size": str(item.get("size") or "tamanho desconhecido"),
                    "model": modelo or "dispositivo removível",
                }
            )

        for filho in item.get("children") or []:
            visitar(filho, removivel, modelo)

    for dispositivo in dados.get("blockdevices") or []:
        visitar(dispositivo)

    return sorted(candidatas, key=lambda item: item["path"])


def listar_particoes_removiveis() -> list[dict[str, str]]:
    if shutil.which("lsblk") is None:
        raise RuntimeError("O comando lsblk não está disponível neste sistema.")

    processo = subprocess.run(
        [
            "lsblk",
            "--json",
            "--output",
            "PATH,TYPE,RM,RO,SIZE,MODEL,MOUNTPOINTS",
        ],
        check=True,
        capture_output=True,
        text=True,
    )
    return extrair_particoes_seguras(json.loads(processo.stdout))


class FormatadorPendrive(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("Formatar pendrive com segurança")
        self.geometry("620x330")
        self.candidatas: list[dict[str, str]] = []

        tk.Label(
            self,
            text="Somente partições removíveis e desmontadas são exibidas.",
            wraplength=560,
            justify=tk.LEFT,
        ).pack(padx=20, pady=(20, 8), anchor=tk.W)

        self.lista = tk.Listbox(self, width=82, height=8, exportselection=False)
        self.lista.pack(padx=20, pady=8, fill=tk.BOTH, expand=True)

        botoes = tk.Frame(self)
        botoes.pack(padx=20, pady=(4, 18), fill=tk.X)
        tk.Button(botoes, text="Atualizar lista", command=self.atualizar).pack(
            side=tk.LEFT
        )
        tk.Button(
            botoes,
            text="Formatar em EXT4",
            command=self.formatar_selecionada,
        ).pack(side=tk.LEFT, padx=8)
        tk.Button(botoes, text="Fechar", command=self.destroy).pack(side=tk.RIGHT)

        self.atualizar()

    def atualizar(self) -> None:
        self.lista.delete(0, tk.END)
        try:
            self.candidatas = listar_particoes_removiveis()
        except (json.JSONDecodeError, OSError, subprocess.SubprocessError) as erro:
            self.candidatas = []
            messagebox.showerror("Não foi possível listar os dispositivos", str(erro))
            return

        if not self.candidatas:
            self.lista.insert(
                tk.END,
                "Nenhuma partição USB removível, gravável e desmontada encontrada.",
            )
            return

        for item in self.candidatas:
            self.lista.insert(
                tk.END,
                f'{item["path"]} — {item["size"]} — {item["model"]}',
            )

    def formatar_selecionada(self) -> None:
        selecao = self.lista.curselection()
        if not selecao or not self.candidatas:
            messagebox.showwarning("Selecione uma partição", "Nada foi formatado.")
            return

        caminho = self.candidatas[selecao[0]]["path"]
        aviso = (
            f"Esta operação apagará permanentemente todos os dados de {caminho}.\n\n"
            "Confirme somente se você identificou fisicamente o pendrive correto."
        )
        if not messagebox.askyesno("Confirmação obrigatória", aviso, icon="warning"):
            return

        frase = f"FORMATAR {caminho}"
        digitado = simpledialog.askstring(
            "Última confirmação",
            f"Digite exatamente:\n{frase}",
            parent=self,
        )
        if digitado != frase:
            messagebox.showinfo("Operação cancelada", "A frase não conferiu.")
            return

        try:
            atuais = {item["path"] for item in listar_particoes_removiveis()}
        except (json.JSONDecodeError, OSError, subprocess.SubprocessError) as erro:
            messagebox.showerror("Verificação falhou", str(erro))
            return
        if caminho not in atuais:
            messagebox.showerror(
                "Dispositivo mudou",
                "A partição não está mais segura ou disponível. Nada foi formatado.",
            )
            self.atualizar()
            return

        comando = ["mkfs.ext4", "-F", caminho]
        if getattr(os, "geteuid", lambda: 1)() != 0:
            if shutil.which("pkexec") is None:
                messagebox.showerror(
                    "Permissão necessária",
                    "Instale/configure o pkexec ou execute este programa como administrador.",
                )
                return
            comando.insert(0, "pkexec")

        try:
            subprocess.run(comando, check=True, capture_output=True, text=True)
        except FileNotFoundError:
            messagebox.showerror("Comando indisponível", "mkfs.ext4 não foi encontrado.")
        except subprocess.CalledProcessError as erro:
            detalhe = (erro.stderr or erro.stdout or "Erro sem detalhes").strip()
            messagebox.showerror("Formatação não concluída", detalhe[-1200:])
        else:
            messagebox.showinfo(
                "Formatação concluída",
                f"A partição {caminho} foi formatada em EXT4.",
            )
            self.atualizar()


if __name__ == "__main__":
    FormatadorPendrive().mainloop()
