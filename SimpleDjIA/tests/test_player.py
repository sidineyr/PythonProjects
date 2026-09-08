from simple_djia import player


def test_detect_backend_prefers_mpv(monkeypatch):
    monkeypatch.setattr(player.shutil, "which", lambda exe: "/usr/bin/mpv" if exe == "mpv" else None)
    backend = player.detect_backend()
    assert backend is not None
    assert backend.name == "mpv"


def test_detect_backend_returns_none_without_supported_players(monkeypatch):
    monkeypatch.setattr(player.shutil, "which", lambda exe: None)
    assert player.detect_backend() is None
