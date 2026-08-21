"""Command-line interface for Python Music Composer."""

import argparse

from music_composer.composer import compose_melody
from music_composer.harmony import PROGRESSIONS, build_accompaniment
from music_composer.midi import write_midi

TIME_SIGNATURES = {"4/4": 4, "3/4": 3, "2/4": 2}


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Generate a harmony-aware MIDI composition.")
    parser.add_argument("--root", default="C")
    parser.add_argument("--scale", choices=("major", "minor"), default="major")
    parser.add_argument("--octave", type=int, default=4)
    parser.add_argument("--bars", type=int, default=8)
    parser.add_argument("--time-signature", choices=tuple(TIME_SIGNATURES), default="4/4")
    parser.add_argument("--tempo", type=int, default=100)
    parser.add_argument("--instrument", type=int, default=0)
    parser.add_argument("--progression", choices=tuple(PROGRESSIONS), default="I-V-vi-IV")
    parser.add_argument("--no-accompaniment", action="store_true")
    parser.add_argument("--randomness", type=float, default=0.45)
    parser.add_argument("--seed", type=int)
    parser.add_argument("--output", default="composition.mid")
    return parser


def main() -> None:
    args = build_parser().parse_args()
    beats = TIME_SIGNATURES[args.time_signature]
    melody = compose_melody(args.root, args.scale, args.octave, args.bars, beats, args.randomness, args.seed, args.progression)
    chords, bass = ([], [])
    if not args.no_accompaniment:
        chords, bass = build_accompaniment(args.root, args.scale, args.bars, beats, args.progression)
    path = write_midi(melody, args.output, args.tempo, args.instrument, chords, bass, beats)
    print(f"Created {path}: {len(melody)} melody notes, {len(chords)} chords, {len(bass)} bass notes.")


if __name__ == "__main__":
    main()
