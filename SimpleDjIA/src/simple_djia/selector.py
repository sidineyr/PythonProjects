from __future__ import annotations

from .models import RankedTrack, SceneProfile, Track

FEATURES = ("energy", "valence", "acousticness", "danceability", "familiarity")


def score_track(track: Track, scene: SceneProfile) -> RankedTrack:
    tags = set(track.tags)
    if tags.intersection(scene.avoid_tags):
        return RankedTrack(track, -999.0, ("blocked by avoid tag",))
    if scene.max_vocal_presence is not None and track.vocal_presence > scene.max_vocal_presence:
        return RankedTrack(track, -999.0, ("too much vocal presence for scene",))

    score = 1.0
    reasons: list[str] = []
    bpm_distance = abs(track.bpm - scene.target_bpm) / max(scene.bpm_tolerance, 1)
    score -= min(bpm_distance, 2.0) * 0.7
    if bpm_distance <= 0.5:
        reasons.append("tempo fits scene")

    for feature in FEATURES:
        target = scene.targets.get(feature, 0.5)
        weight = scene.weights.get(feature, 1.0)
        distance = abs(getattr(track, feature) - target)
        score -= distance * weight
        if distance <= 0.15:
            reasons.append(f"{feature} near target")

    preferred = tags.intersection(scene.preferred_tags)
    score += 0.18 * len(preferred)
    if preferred:
        reasons.append("preferred tags: " + ", ".join(sorted(preferred)))
    return RankedTrack(track, score, tuple(reasons))


def _transition_cost(a: Track, b: Track) -> float:
    bpm = min(abs(a.bpm - b.bpm) / 60.0, 1.0)
    energy = abs(a.energy - b.energy)
    valence = abs(a.valence - b.valence)
    return 0.45 * bpm + 0.35 * energy + 0.20 * valence


def build_playlist(tracks: list[Track], scene: SceneProfile, limit: int = 20) -> list[RankedTrack]:
    """Rank transparently, then sequence with artist diversity and gradual transitions."""
    if limit < 1:
        raise ValueError("limit must be at least 1")

    pool = [r for r in (score_track(t, scene) for t in tracks) if r.score > -900]
    pool.sort(key=lambda item: item.score, reverse=True)
    if not pool:
        return []

    result: list[RankedTrack] = [pool.pop(0)]
    while pool and len(result) < limit:
        previous = result[-1].track
        candidates = sorted(
            pool,
            key=lambda item: (
                item.track.artist == previous.artist,
                _transition_cost(previous, item.track) > scene.transition_limit,
                _transition_cost(previous, item.track),
                -item.score,
            ),
        )
        chosen = candidates[0]
        result.append(chosen)
        pool.remove(chosen)
    return result
