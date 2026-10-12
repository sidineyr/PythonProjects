#!/usr/bin/env bash
set -euo pipefail

PASTA="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
MIDI="$PASTA/saida_da_caverna.mid"
WAV="$PASTA/saida_da_caverna.wav"
SOUNDFONT="${SOUNDFONT:-/usr/share/sounds/sf2/FluidR3_GM.sf2}"

python3 "$PASTA/saida_da_caverna.py"

if ! command -v fluidsynth >/dev/null 2>&1; then
  echo "FluidSynth não encontrado. Instale-o e execute novamente." >&2
  exit 1
fi

if [[ ! -f "$SOUNDFONT" ]]; then
  echo "SoundFont não encontrada em: $SOUNDFONT" >&2
  echo "Informe outra com: SOUNDFONT=/caminho/piano.sf2 ./renderizar.sh" >&2
  exit 1
fi

fluidsynth -ni "$SOUNDFONT" "$MIDI" -F "$WAV" -r 44100 -g 0.65
echo "Áudio criado: $WAV"
