package br.com.sidineyr.somente

data class AdState(
    val completedLessons: Int,
    val adsToday: Int,
    val lastAdAtMs: Long,
    val isFirstSession: Boolean,
    val audioPlaying: Boolean
)

object AdPolicy {
    const val LESSON_INTERVAL = 4
    const val MIN_INTERVAL_MS = 12 * 60 * 1000L
    const val DAILY_LIMIT = 3

    fun canShowAfterLesson(state: AdState, nowMs: Long): Boolean =
        !state.isFirstSession &&
            !state.audioPlaying &&
            state.completedLessons > 0 &&
            state.completedLessons % LESSON_INTERVAL == 0 &&
            state.adsToday < DAILY_LIMIT &&
            nowMs - state.lastAdAtMs >= MIN_INTERVAL_MS
}
