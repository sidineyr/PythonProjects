package br.com.sidineyr.somente

import android.graphics.Color
import android.os.Bundle
import android.view.Gravity
import android.view.View
import android.widget.Button
import android.widget.LinearLayout
import android.widget.ProgressBar
import android.widget.ScrollView
import android.widget.TextView
import androidx.appcompat.app.AppCompatActivity
import kotlin.random.Random

class MainActivity : AppCompatActivity() {
    private val player = TonePlayer()
    private lateinit var ads: AdController
    private lateinit var root: LinearLayout
    private val prefs by lazy { getSharedPreferences("progress", MODE_PRIVATE) }
    private var lessonIndex = 0
    private var expected = ""
    private var firstSession = true

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        ads = AdController(this)
        firstSession = !prefs.getBoolean("has_finished_session", false)
        lessonIndex = prefs.getInt("lesson", 0).coerceIn(0, Curriculum.lessons.lastIndex)
        root = LinearLayout(this).apply {
            orientation = LinearLayout.VERTICAL
            gravity = Gravity.CENTER_HORIZONTAL
            setPadding(40, 52, 40, 40)
            setBackgroundColor(Color.rgb(23, 21, 42))
        }
        setContentView(ScrollView(this).apply { addView(root) })
        showLesson()
        ads.preload()
    }

    private fun showLesson(message: String? = null) {
        root.removeAllViews()
        val lesson = Curriculum.lessons[lessonIndex]
        root.addView(text("SOMENTE", 30, Color.rgb(247, 211, 91)))
        root.addView(text("Som + mente: aprender música escutando", 15, Color.LTGRAY))
        root.addView(ProgressBar(this, null, android.R.attr.progressBarStyleHorizontal).apply {
            max = Curriculum.lessons.size
            progress = lessonIndex + 1
            layoutParams = LinearLayout.LayoutParams(-1, 18).also { it.setMargins(0, 36, 0, 36) }
        })
        root.addView(text("${lessonIndex + 1}. ${lesson.title}", 26, Color.WHITE))
        root.addView(text(lesson.objective, 17, Color.LTGRAY).withMargins(0, 16, 0, 28))
        root.addView(text(lesson.prompt, 20, Color.WHITE).withMargins(0, 8, 0, 28))
        button("▶ Ouvir exemplo") { presentExercise(lesson) }
        lesson.choices.forEach { choice -> button(choice) { answer(lesson, choice) } }
        message?.let { root.addView(text(it, 17, Color.rgb(247, 211, 91)).withMargins(0, 24, 0, 0)) }
        root.addView(text("Sem pressa. Você pode ouvir quantas vezes precisar.", 14, Color.GRAY).withMargins(0, 38, 0, 0))
    }

    private fun presentExercise(lesson: Lesson) {
        if (player.isPlaying()) return
        val (notes, answer, volume) = when (lesson.kind) {
            ExerciseKind.SOUND_OR_SILENCE -> if (Random.nextBoolean()) Triple(listOf(440.0), "Som", .42) else Triple(emptyList(), "Silêncio", .0)
            ExerciseKind.SAME_OR_DIFFERENT -> if (Random.nextBoolean()) Triple(listOf(330.0, 330.0), "Iguais", .42) else Triple(listOf(330.0, 494.0), "Diferentes", .42)
            ExerciseKind.HIGH_OR_LOW -> if (Random.nextBoolean()) Triple(listOf(220.0), "Grave", .45) else Triple(listOf(880.0), "Agudo", .40)
            ExerciseKind.LOUD_OR_SOFT -> if (Random.nextBoolean()) Triple(listOf(440.0), "Forte", .72) else Triple(listOf(440.0), "Fraco", .18)
            ExerciseKind.PULSE -> Triple(listOf(440.0, 440.0, 440.0, 440.0), "Marcar pulso", .42)
            ExerciseKind.RHYTHM -> Triple(listOf(392.0, 392.0, 523.25), "Repetir ritmo", .42)
            ExerciseKind.NOTE -> Triple(listOf(261.63), "Reconheci", .42)
            ExerciseKind.MELODY -> if (Random.nextBoolean()) Triple(listOf(261.63, 329.63, 392.0), "Subiu", .42) else Triple(listOf(392.0, 329.63, 261.63), "Desceu", .42)
        }
        expected = answer
        if (notes.isEmpty()) window.decorView.postDelayed({ expected = answer }, 650) else player.play(notes, volume)
    }

    private fun answer(lesson: Lesson, choice: String) {
        if (expected.isBlank()) { showLesson("Primeiro ouça o exemplo."); return }
        if (choice != expected && lesson.kind !in setOf(ExerciseKind.PULSE, ExerciseKind.RHYTHM, ExerciseKind.NOTE)) {
            showLesson("Ainda não. Ouça novamente e compare — errar também treina o ouvido.")
            return
        }
        val completed = prefs.getInt("completed", 0) + 1
        val next = (lessonIndex + 1).coerceAtMost(Curriculum.lessons.lastIndex)
        prefs.edit().putInt("completed", completed).putInt("lesson", next).apply()
        lessonIndex = next
        expected = ""
        val now = System.currentTimeMillis()
        val today = java.time.LocalDate.now().toString()
        val adsToday = if (prefs.getString("ad_day", "") == today) prefs.getInt("ads_today", 0) else 0
        if (adsToday == 0) prefs.edit().putString("ad_day", today).putInt("ads_today", 0).apply()
        val state = AdState(completed, adsToday, prefs.getLong("last_ad", 0), firstSession, player.isPlaying())
        if (AdPolicy.canShowAfterLesson(state, now) && ads.showIfReady {
                prefs.edit().putInt("ads_today", state.adsToday + 1).putLong("last_ad", now).apply()
                showLesson("Muito bem! Vamos ao próximo passo.")
            }) return
        showLesson("Muito bem! Vamos ao próximo passo.")
    }

    override fun onStop() {
        prefs.edit().putBoolean("has_finished_session", true).apply()
        super.onStop()
    }

    private fun button(label: String, action: () -> Unit) {
        root.addView(Button(this).apply {
            text = label
            isAllCaps = false
            textSize = 17f
            setOnClickListener { action() }
            layoutParams = LinearLayout.LayoutParams(-1, -2).also { it.setMargins(0, 8, 0, 8) }
        })
    }

    private fun text(value: String, size: Int, color: Int) = TextView(this).apply {
        text = value; textSize = size.toFloat(); setTextColor(color); gravity = Gravity.CENTER
        importantForAccessibility = View.IMPORTANT_FOR_ACCESSIBILITY_YES
    }

    private fun View.withMargins(l: Int, t: Int, r: Int, b: Int): View = apply {
        layoutParams = LinearLayout.LayoutParams(-1, -2).also { it.setMargins(l, t, r, b) }
    }
}
