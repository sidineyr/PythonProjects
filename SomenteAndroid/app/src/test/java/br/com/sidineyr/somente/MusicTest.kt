package br.com.sidineyr.somente

import org.junit.Assert.assertEquals
import org.junit.Assert.assertTrue
import org.junit.Test

class MusicTest {
    @Test fun `note frequencies and staff positions rise together`() {
        assertTrue(Music.notes.zipWithNext().all { (a, b) -> a.frequency < b.frequency && a.staffStep < b.staffStep })
    }

    @Test fun `saved teacher exercise survives round trip`() {
        val original = listOf(Music.notes[0], Music.notes[2], Music.notes[4])
        assertEquals(original, Music.decode(Music.encode(original)))
    }

    @Test fun `invalid saved values are ignored`() {
        assertEquals(listOf(Music.notes[0]), Music.decode("0,x,99"))
    }

    @Test fun `examples remain short enough for a beginner screen`() {
        assertTrue(Music.examples.all { it.notes.isNotEmpty() && it.notes.size <= 16 })
    }
}
