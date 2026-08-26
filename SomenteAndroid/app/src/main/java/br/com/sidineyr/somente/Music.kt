package br.com.sidineyr.somente

data class MusicNote(val name: String, val frequency: Double, val staffStep: Int)

data class MusicSequence(val title: String, val notes: List<MusicNote>)

object Music {
    val notes = listOf(
        MusicNote("Dó", 261.63, 0), MusicNote("Ré", 293.66, 1),
        MusicNote("Mi", 329.63, 2), MusicNote("Fá", 349.23, 3),
        MusicNote("Sol", 392.00, 4), MusicNote("Lá", 440.00, 5),
        MusicNote("Si", 493.88, 6), MusicNote("Dó↑", 523.25, 7)
    )

    val examples = listOf(
        MusicSequence("Escada sonora", notes.take(8)),
        MusicSequence("Três notas", listOf(notes[0], notes[2], notes[4], notes[2], notes[0])),
        MusicSequence("Pergunta e resposta", listOf(notes[0], notes[1], notes[2], notes[4], notes[2], notes[1], notes[0]))
    )

    fun encode(sequence: List<MusicNote>) = sequence.joinToString(",") { notes.indexOf(it).toString() }

    fun decode(value: String): List<MusicNote> = value.split(',').mapNotNull {
        it.toIntOrNull()?.let { index -> notes.getOrNull(index) }
    }
}
