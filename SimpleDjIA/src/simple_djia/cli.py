from __future__ import annotations

import argparse

from .library import load_library
from .profiles import SCENES, get_scene
from .session import create_session, play_session


def parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="simple-djia", description="Human-centered ambient DJ for open platforms")
    p.add_argument("library", help="JSON music library")
    p.add_argument("--scene", choices=tuple(SCENES), default="restaurant_piano")
    p.add_argument("--limit", type=int, default=12)
    p.add_argument("--play", action="store_true", help="play the generated list using mpv/VLC/ffplay")
    return p


def main() -> None:
    args = parser().parse_args()
    tracks = load_library(args.library)
    scene = get_scene(args.scene)
    session = create_session(tracks, scene, args.limit)
    print(f"\nSimple DjIA — {scene.name}\n{scene.description}\n")
    if not session.playlist:
        print("No compatible tracks found for this scene.")
        raise SystemExit(2)
    for i, ranked in enumerate(session.playlist, 1):
        t = ranked.track
        why = "; ".join(ranked.reasons[:3]) or "balanced scene fit"
        print(f"{i:02d}. {t.artist} — {t.title} | {t.bpm:g} BPM | score {ranked.score:.2f} | {why}")
    if args.play:
        play_session(session)


if __name__ == "__main__":
    main()
