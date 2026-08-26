package br.com.sidineyr.somente

import android.media.AudioAttributes
import android.media.AudioFormat
import android.media.AudioTrack
import kotlin.concurrent.thread
import kotlin.math.PI
import kotlin.math.sin

class TonePlayer {
    @Volatile private var playing = false

    fun play(notes: List<MusicNote>, noteMs: Int = 520, onNote: (Int) -> Unit = {}, onDone: () -> Unit = {}) {
        if (playing || notes.isEmpty()) return
        playing = true
        thread(name = "somente-tone") {
            try { notes.forEachIndexed { index, note -> onNote(index); playOne(note.frequency, noteMs) } }
            finally { playing = false; onDone() }
        }
    }

    fun isPlaying() = playing

    private fun playOne(frequency: Double, durationMs: Int) {
        val sampleRate = 44_100
        val count = sampleRate * durationMs / 1000
        val samples = ShortArray(count) { index ->
            val fade = minOf(1.0, index / 500.0, (count - index) / 500.0)
            (sin(2.0 * PI * index * frequency / sampleRate) * Short.MAX_VALUE * .42 * fade).toInt().toShort()
        }
        val track = AudioTrack.Builder()
            .setAudioAttributes(AudioAttributes.Builder().setUsage(AudioAttributes.USAGE_MEDIA).setContentType(AudioAttributes.CONTENT_TYPE_MUSIC).build())
            .setAudioFormat(AudioFormat.Builder().setSampleRate(sampleRate).setEncoding(AudioFormat.ENCODING_PCM_16BIT).setChannelMask(AudioFormat.CHANNEL_OUT_MONO).build())
            .setBufferSizeInBytes(samples.size * 2).setTransferMode(AudioTrack.MODE_STATIC).build()
        track.write(samples, 0, samples.size)
        track.play()
        Thread.sleep(durationMs.toLong() + 25)
        track.stop()
        track.release()
    }
}
