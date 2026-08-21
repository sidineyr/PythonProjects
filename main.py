"""Command-line interface for Python Music Composer."""

import argparse

from music_composer.composer import compose_melody
from music_composer.midi import write_midi


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Generate a scale-aware MIDI melody.")
    parser.add_argument("--root", default="C", help="Root note, e.g. C, D, F#")
    parser.add_argument("--scale", choices=("major", "minor"), default="major")
    parser.add_argument("--octave", type=int, default=4)
    parser.add_argument("--bars", type=int, default=4)
    parser.add_argument("--beats", type=int, default=4, help="Beats per bar")
    parser.add_argument("--tempo", type=int, default=120)
    parser.add_argument("--instrument", type=int, default=0, help="General MIDI program 0-127")
    parser.add_argument("--randomness", type=float, default=0.5)
    parser.add_argument("--seed", type=int)
    parser.add_argument("--output", default="composition.mid")
    return parser


def main() -> None:
    args = build_parser().parse_args()
    melody = compose_melody(
        root=args.root,
        scale=args.scale,
        octave=args.octave,
        bars=args.bars,
        beats_per_bar=args.beats,
        randomness=args.randomness,
        seed=args.seed,
    )
    path = write_midi(melody, args.output, args.tempo, args.instrument)
    print(f"Created {path} with {len(melody)} notes.")


if __name__ == "__main__":
    main()
