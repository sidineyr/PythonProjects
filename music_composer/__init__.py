"""Core package for Python Music Composer."""

from .composer import MelodyEvent, compose_melody
from .theory import scale_pitch_classes

__all__ = ["MelodyEvent", "compose_melody", "scale_pitch_classes"]
