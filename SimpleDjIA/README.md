# Simple DjIA

**Simple DjIA** is an open-source, human-centered music programming application for Linux and other open platforms. It behaves like a contextual musician: a discreet pianist in a restaurant, an energetic DJ at a party, a calm background selector, or a focus-oriented ambient curator.

The project deliberately keeps musical decisions transparent. It does **not** claim to replace a human DJ, musician, therapist, or clinical music therapist. Its wellbeing-oriented profiles are inspired by human listening, context, familiarity, gradual change, and respect for the people in the room.

## Philosophy

A playlist is not just a ranking problem. Human listeners notice repetition, sudden changes, excessive volume/energy, intrusive vocals, familiarity, silence, and the social function of a place. Simple DjIA therefore uses explicit criteria rather than a hidden recommendation model.

Each track can carry human-readable metadata:

- tempo/BPM
- energy
- valence (pleasant/positive affect proxy)
- acousticness
- danceability
- vocal presence
- familiarity
- tags such as `piano`, `instrumental`, `house`, `ambient`, `bossa`

Each behavior profile describes a desired musical environment and the selector explains why tracks fit it.

## Included behaviors

- `restaurant_piano` — discreet piano/acoustic background for conversation
- `mega_party_dj` — high-energy dance-oriented sequencing
- `calm_connection` — gentle, low-overload listening inspired by human connection
- `focus_background` — restrained instrumental background with low vocal presence

Profiles live in `src/simple_djia/profiles.py`, so interested users can copy, inspect, modify, or create their own.

## Open-platform design

The Python core uses only the standard library. Audio playback is delegated to established open tools, detected in this order:

1. `mpv`
2. `cvlc` (VLC)
3. `ffplay` (FFmpeg)

This avoids binding the application to proprietary codecs, stores, streaming APIs, DRM, or closed operating-system frameworks. OGG, FLAC, WAV and other formats supported by the installed player are recommended. Users are responsible for the rights to music they add.

## Requirements

- Python 3.10+
- Linux recommended
- Tk/Tkinter for the desktop interface
- optional playback backend: MPV, VLC, or FFmpeg

Debian/Ubuntu example:

```bash
sudo apt install python3 python3-tk mpv
```

Fedora example:

```bash
sudo dnf install python3 python3-tkinter mpv
```

Arch Linux example:

```bash
sudo pacman -S python tk mpv
```

## Install

From the `SimpleDjIA` directory:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -e .
```

No runtime Python dependencies beyond the standard library are required.

## Create a library

Copy `examples/library.example.json` and point each entry to audio that you are legally allowed to play. Relative paths are resolved from the JSON file location.

Example:

```json
{
  "path": "./music/song.ogg",
  "title": "Song",
  "artist": "Artist",
  "genre": "piano",
  "bpm": 82,
  "energy": 0.30,
  "valence": 0.60,
  "acousticness": 0.90,
  "danceability": 0.20,
  "vocal_presence": 0.00,
  "familiarity": 0.50,
  "tags": ["piano", "instrumental"]
}
```

All normalized values use the range `0.0` to `1.0`.

## Command line

Preview a restaurant playlist:

```bash
simple-djia examples/library.example.json --scene restaurant_piano --limit 12
```

Build and play a party session:

```bash
simple-djia examples/library.example.json --scene mega_party_dj --limit 25 --play
```

## Desktop menu

```bash
simple-djia-gui
```

Choose a JSON library, select the desired behavior, choose playlist length, then generate the ordered playlist.

## How selection works

1. Tracks carrying explicitly avoided tags are removed.
2. Vocal-density limits are respected for contexts where speech/conversation matters.
3. BPM is compared with the scene's target and tolerance.
4. Human-readable features are compared with scene targets using explicit weights.
5. Preferred tags add a small bonus.
6. The resulting candidates are re-ordered to reduce abrupt BPM/energy/valence changes.
7. Consecutive tracks by the same artist are avoided when a reasonable alternative exists.

There is no opaque model deciding what a person is supposed to feel. The scoring rules are ordinary Python and can be inspected or changed.

## Testing and compatibility

Run locally:

```bash
pip install pytest
pytest -q
python -m compileall -q src
simple-djia --help
```

The repository includes a GitHub Actions matrix for Python 3.10, 3.11, 3.12 and 3.13 on Ubuntu Linux.

## Project layout

```text
SimpleDjIA/
├── pyproject.toml
├── README.md
├── LICENSE
├── examples/
│   └── library.example.json
├── src/simple_djia/
│   ├── cli.py
│   ├── gui.py
│   ├── library.py
│   ├── models.py
│   ├── player.py
│   ├── profiles.py
│   ├── selector.py
│   └── session.py
└── tests/
    ├── test_library.py
    ├── test_models.py
    └── test_selector.py
```

## Roadmap

The first release intentionally favors understandable rules over hype. Useful later additions include manual feedback controls (`more calm`, `more dance`, `less vocal`), local audio-feature extraction, MIDI/live-piano generation using the existing Python Music Composer work, crossfades via MPV IPC, room/session history stored locally, and optional local-only machine learning whose recommendations remain explainable and user-overridable.

## License

MIT. See `LICENSE`.
