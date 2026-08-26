package br.com.sidineyr.somente

import org.junit.Assert.assertEquals
import org.junit.Assert.assertTrue
import org.junit.Test

class CurriculumTest {
    @Test fun `listening precedes notation`() {
        val kinds = Curriculum.lessons.map { it.kind }
        assertTrue(kinds.indexOf(ExerciseKind.HIGH_OR_LOW) < kinds.indexOf(ExerciseKind.NOTE))
        assertTrue(kinds.indexOf(ExerciseKind.PULSE) < kinds.indexOf(ExerciseKind.MELODY))
    }

    @Test fun `lesson ids are unique`() {
        assertEquals(Curriculum.lessons.size, Curriculum.lessons.map { it.id }.toSet().size)
    }
}
