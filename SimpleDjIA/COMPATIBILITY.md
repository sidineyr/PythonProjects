# Simple DjIA compatibility report

Validation performed during the v0.1 development pass.

## Local Linux validation

Environment used by the development runner:

- Linux
- CPython 3.13.5
- Tk 8.6 available
- pytest 9.0.2
- ffplay available as an open playback backend

Results:

- `python -m compileall -q src`: PASS
- unit tests: **9 passed**
- CLI smoke test (`python -m simple_djia.cli --help`): PASS
- Tkinter/GUI module import: PASS
- player discovery: PASS; ffplay detected in the validation environment
- editable installation: PASS when build isolation is disabled in the network-isolated development runner (`pip --no-build-isolation -e .`)

The normal install documented in the README remains `pip install -e .`; it requires access to Python package infrastructure only to satisfy the standard build backend requirement if it is not already installed.

## Python grammar compatibility

Every Python source file was parsed using CPython's versioned grammar compatibility mode for:

- Python 3.10: PASS
- Python 3.11: PASS
- Python 3.12: PASS
- Python 3.13: PASS

The application intentionally uses only standard-library runtime APIs that are available across this range.

## GitHub Actions

A dedicated Ubuntu matrix is committed for Python 3.10, 3.11, 3.12 and 3.13. During this development session, GitHub created all four jobs but reported each as failed before exposing any executed steps or job log blob. Because the jobs did not reach a visible test step, this cannot be treated as a source-code test failure. The workflow remains in the repository so it can execute normally when GitHub-hosted runners are available for the account/repository.

The legacy root `Python application` workflow is isolated from SimpleDjIA-only changes to avoid collecting unrelated historical experiments in this subproject's validation.

## Playback compatibility

Simple DjIA does not embed a proprietary audio engine. It discovers, in order:

1. MPV (`mpv`)
2. VLC (`cvlc`)
3. FFmpeg player (`ffplay`)

Actual codec support therefore follows the selected backend. OGG/Vorbis, FLAC and WAV are recommended for an open workflow.

## Known v0.1 limits

- audio features are human-supplied metadata; automatic feature extraction is a later enhancement;
- no crossfade/mixing engine yet;
- GUI playback is intentionally simple: selected track, next track and stop;
- no streaming-service or DRM integration by design;
- wellbeing-oriented profiles are contextual curation tools and are not clinical music therapy.
