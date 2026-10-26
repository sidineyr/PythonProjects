#!/usr/bin/env bash
set -euo pipefail

PASTA="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SOUNDFONT="${SOUNDFONT:-/usr/share/sounds/sf2/FluidR3_GM.sf2}"
FLUIDSYNTH="${FLUIDSYNTH:-fluidsynth}"

python3 "$PASTA/finais.py"
command -v "$FLUIDSYNTH" >/dev/null 2>&1 || { echo "FluidSynth não encontrado." >&2; exit 1; }
[[ -f "$SOUNDFONT" ]] || { echo "SoundFont não encontrada: $SOUNDFONT" >&2; exit 1; }

for nome in luminoso suspenso sereno; do
  "$FLUIDSYNTH" -ni "$SOUNDFONT" "$PASTA/final_${nome}.mid" \
    -F "$PASTA/final_${nome}.wav" -r 44100 -g 0.65
done
python3 "$PASTA/montar_comparacao.py"
