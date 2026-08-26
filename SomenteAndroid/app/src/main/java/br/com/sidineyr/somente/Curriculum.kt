package br.com.sidineyr.somente

enum class ExerciseKind { SOUND_OR_SILENCE, SAME_OR_DIFFERENT, HIGH_OR_LOW, LOUD_OR_SOFT, PULSE, RHYTHM, NOTE, MELODY }

data class Lesson(
    val id: String,
    val title: String,
    val objective: String,
    val prompt: String,
    val kind: ExerciseKind,
    val choices: List<String>
)

object Curriculum {
    val lessons = listOf(
        Lesson("escuta-1", "Som e silêncio", "Perceber quando existe vibração audível.", "Você ouviu um som?", ExerciseKind.SOUND_OR_SILENCE, listOf("Som", "Silêncio")),
        Lesson("escuta-2", "Igual ou diferente?", "Comparar dois eventos sonoros sem exigir nomes técnicos.", "Os dois sons foram iguais?", ExerciseKind.SAME_OR_DIFFERENT, listOf("Iguais", "Diferentes")),
        Lesson("altura-1", "Grave e agudo", "Reconhecer altura antes de conhecer nomes de notas.", "O som foi grave ou agudo?", ExerciseKind.HIGH_OR_LOW, listOf("Grave", "Agudo")),
        Lesson("intensidade-1", "Forte e fraco", "Distinguir intensidade de altura.", "O som foi forte ou fraco?", ExerciseKind.LOUD_OR_SOFT, listOf("Forte", "Fraco")),
        Lesson("ritmo-1", "Encontre o pulso", "Sentir uma sequência regular de batidas.", "Toque junto com o pulso quatro vezes.", ExerciseKind.PULSE, listOf("Marcar pulso")),
        Lesson("ritmo-2", "Imite o ritmo", "Perceber que ritmo combina durações e pausas.", "Ouça e repita o desenho rítmico.", ExerciseKind.RHYTHM, listOf("Repetir ritmo")),
        Lesson("notas-1", "Uma nota tem nome", "Relacionar uma altura já percebida ao nome Dó.", "Esta nota é Dó. Ouça e reconheça.", ExerciseKind.NOTE, listOf("Ouvir Dó", "Reconheci")),
        Lesson("melodia-1", "Notas em caminho", "Compreender melodia como sequência intencional de alturas e durações.", "A sequência subiu ou desceu?", ExerciseKind.MELODY, listOf("Subiu", "Desceu"))
    )
}
