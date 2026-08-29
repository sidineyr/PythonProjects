from pathlib import Path
import pytest

from simple_djia.models import Track


def test_feature_bounds_are_enforced():
    with pytest.raises(ValueError):
        Track(Path("a.ogg"), "A", energy=1.2)


def test_bpm_bounds_are_enforced():
    with pytest.raises(ValueError):
        Track(Path("a.ogg"), "A", bpm=500)
