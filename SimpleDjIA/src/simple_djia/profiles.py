from .models import SceneProfile


SCENES: dict[str, SceneProfile] = {
    "restaurant_piano": SceneProfile(
        key="restaurant_piano",
        name="Pianista no restaurante",
        description="Fundo elegante, conversável e pouco intrusivo; prioriza piano, acústico e transições suaves.",
        target_bpm=82,
        bpm_tolerance=26,
        targets={"energy": 0.30, "valence": 0.58, "acousticness": 0.90, "danceability": 0.25, "familiarity": 0.55},
        weights={"energy": 1.5, "valence": 0.8, "acousticness": 1.6, "danceability": 0.5, "familiarity": 0.7},
        preferred_tags=("piano", "instrumental", "acoustic", "jazz", "bossa"),
        avoid_tags=("aggressive", "explicit", "distorted"),
        max_vocal_presence=0.35,
        transition_limit=0.22,
    ),
    "mega_party_dj": SceneProfile(
        key="mega_party_dj",
        name="DJ de festa intensa",
        description="Alta energia e dança, com progressão controlada para evitar saltos bruscos de sensação.",
        target_bpm=126,
        bpm_tolerance=18,
        targets={"energy": 0.88, "valence": 0.78, "acousticness": 0.12, "danceability": 0.92, "familiarity": 0.65},
        weights={"energy": 1.8, "valence": 0.8, "acousticness": 0.5, "danceability": 2.0, "familiarity": 0.5},
        preferred_tags=("dance", "house", "electronic", "party"),
        avoid_tags=("sleep", "meditation"),
        transition_limit=0.30,
    ),
    "calm_connection": SceneProfile(
        key="calm_connection",
        name="Conexão calma",
        description="Curadoria de baixa sobrecarga inspirada em escuta humana e vínculo; não substitui musicoterapia clínica.",
        target_bpm=72,
        bpm_tolerance=22,
        targets={"energy": 0.22, "valence": 0.62, "acousticness": 0.78, "danceability": 0.18, "familiarity": 0.62},
        weights={"energy": 1.7, "valence": 1.2, "acousticness": 1.2, "danceability": 0.4, "familiarity": 1.0},
        preferred_tags=("gentle", "acoustic", "piano", "ambient", "instrumental"),
        avoid_tags=("aggressive", "explicit", "harsh"),
        max_vocal_presence=0.55,
        transition_limit=0.18,
    ),
    "focus_background": SceneProfile(
        key="focus_background",
        name="Fundo para foco",
        description="Música previsível e discreta, com preferência por instrumental e baixa presença vocal.",
        target_bpm=88,
        bpm_tolerance=25,
        targets={"energy": 0.35, "valence": 0.52, "acousticness": 0.62, "danceability": 0.20, "familiarity": 0.45},
        weights={"energy": 1.2, "valence": 0.5, "acousticness": 0.8, "danceability": 0.5, "familiarity": 0.4},
        preferred_tags=("instrumental", "ambient", "piano", "lofi"),
        avoid_tags=("aggressive", "explicit"),
        max_vocal_presence=0.25,
        transition_limit=0.20,
    ),
}


def get_scene(key: str) -> SceneProfile:
    try:
        return SCENES[key]
    except KeyError as exc:
        raise ValueError(f"Unknown scene: {key}") from exc
