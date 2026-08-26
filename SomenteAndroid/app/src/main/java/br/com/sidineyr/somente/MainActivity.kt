package br.com.sidineyr.somente

import android.graphics.Color
import android.os.Bundle
import android.view.Gravity
import android.view.View
import android.widget.Button
import android.widget.LinearLayout
import android.widget.ScrollView
import android.widget.TextView
import androidx.appcompat.app.AppCompatActivity
import kotlin.random.Random

class MainActivity : AppCompatActivity() {
    private val player = TonePlayer()
    private lateinit var root: LinearLayout
    private val prefs by lazy { getSharedPreferences("somente", MODE_PRIVATE) }
    private var answerButtons = mutableListOf<Button>()

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        root = LinearLayout(this).apply {
            orientation = LinearLayout.VERTICAL
            gravity = Gravity.CENTER_HORIZONTAL
            setPadding(32, 44, 32, 44)
            setBackgroundColor(Color.rgb(247, 246, 252))
        }
        setContentView(ScrollView(this).apply { addView(root) })
        showHome()
    }

    @Suppress("DEPRECATION")
    override fun onBackPressed() {
        if (root.tag == "home") super.onBackPressed() else showHome()
    }

    private fun showHome() {
        page("home")
        title("SOMENTE")
        subtitle("Ouvir • ler • criar")
        paragraph("Um laboratório musical simples para aprender no próprio ritmo ou usar com um professor.")
        modeButton("👂  Escutar e reconhecer", "Treino auditivo com notas na pauta") { showEarTraining() }
        modeButton("♫  Ler e ouvir", "Acompanhe cada nota enquanto ela toca") { showReader() }
        modeButton("✎  Criar exercício", "Monte e salve uma sequência para sua aula") { showComposer() }
        paragraph("Funciona sem conta, anúncios ou internet. Use fones apenas em volume confortável.", muted = true)
    }

    private fun showEarTraining(message: String? = null) {
        page("ear")
        backButton()
        title("Escutar e reconhecer")
        paragraph("Ouça primeiro. Depois escolha a nota. A pauta revela a resposta.")
        val target = Music.notes[Random.nextInt(7)]
        val staff = StaffView(this).apply { notes = emptyList() }
        root.addView(staff)
        val choices = Music.notes.take(7).shuffled().take(3).toMutableList()
        if (target !in choices) choices[0] = target
        answerButtons.clear()
        button("▶ Ouvir nota") {
            setAnswersEnabled(false)
            player.play(listOf(target), onDone = { runOnUiThread { setAnswersEnabled(true) } })
        }
        choices.shuffled().forEach { candidate ->
            answerButtons += button(candidate.name, enabled = false) {
                staff.notes = listOf(target)
                setAnswersEnabled(false)
                if (candidate == target) {
                    prefs.edit().putInt("correct", prefs.getInt("correct", 0) + 1).apply()
                    showEarTraining("Muito bem: ${target.name}. Ouça a próxima.")
                } else {
                    setAnswersEnabled(true)
                    toastText("Era ${target.name}. Compare e tente uma nova nota.")
                }
            }
        }
        message?.let(::success)
        paragraph("Acertos nesta instalação: ${prefs.getInt("correct", 0)}", muted = true)
    }

    private fun showReader() {
        page("reader")
        backButton()
        title("Ler e ouvir")
        paragraph("A nota dourada mostra onde a reprodução está. Toque de novo quantas vezes precisar.")
        val custom = Music.decode(prefs.getString("teacher_sequence", "") ?: "")
        val sequences = Music.examples + if (custom.isNotEmpty()) listOf(MusicSequence("Exercício do professor", custom)) else emptyList()
        var selected = sequences.first()
        val staff = StaffView(this).apply { notes = selected.notes }
        root.addView(staff)
        val heading = subtitle(selected.title)
        sequences.forEach { sequence ->
            button(sequence.title) {
                if (!player.isPlaying()) { selected = sequence; heading.text = sequence.title; staff.notes = sequence.notes }
            }
        }
        button("▶ Reproduzir com acompanhamento") {
            if (player.isPlaying()) return@button
            player.play(selected.notes,
                onNote = { runOnUiThread { staff.activeIndex = it } },
                onDone = { runOnUiThread { staff.activeIndex = -1 } })
        }
    }

    private fun showComposer(message: String? = null) {
        page("composer")
        backButton()
        title("Criar exercício")
        paragraph("Professor ou estudante: toque nas notas para montar uma frase de até 16 sons.")
        val sequence = Music.decode(prefs.getString("teacher_sequence", "") ?: "").toMutableList()
        val staff = StaffView(this).apply { notes = sequence.toList() }
        root.addView(staff)
        val summary = subtitle(sequenceSummary(sequence))
        Music.notes.forEach { note ->
            button("+ ${note.name}") {
                if (sequence.size < 16) { sequence += note; staff.notes = sequence.toList(); summary.text = sequenceSummary(sequence) }
                else toastText("O limite é 16 notas para manter o exercício legível.")
            }
        }
        button("▶ Ouvir minha sequência") {
            if (sequence.isEmpty()) toastText("Adicione pelo menos uma nota.") else player.play(sequence)
        }
        button("↶ Desfazer última nota") {
            if (sequence.isNotEmpty()) { sequence.removeAt(sequence.lastIndex); staff.notes = sequence.toList(); summary.text = sequenceSummary(sequence) }
        }
        button("Salvar para usar em aula") {
            if (sequence.isEmpty()) toastText("Crie uma sequência antes de salvar.")
            else { prefs.edit().putString("teacher_sequence", Music.encode(sequence)).apply(); showComposer("Exercício salvo no aparelho e disponível em “Ler e ouvir”.") }
        }
        message?.let(::success)
    }

    private fun sequenceSummary(notes: List<MusicNote>) = if (notes.isEmpty()) "Sua sequência está vazia" else notes.joinToString("  ") { it.name }
    private fun setAnswersEnabled(enabled: Boolean) { answerButtons.forEach { it.isEnabled = enabled } }
    private fun page(tag: String) { root.removeAllViews(); root.tag = tag; answerButtons.clear() }
    private fun backButton() { button("‹ Início") { showHome() } }
    private fun title(value: String) = text(value, 30, Color.rgb(43, 37, 74)).also { root.addView(it) }
    private fun subtitle(value: String) = text(value, 19, Color.rgb(82, 70, 160)).also { root.addView(it) }
    private fun paragraph(value: String, muted: Boolean = false) = text(value, 16, if (muted) Color.GRAY else Color.DKGRAY).also { it.setPadding(0, 18, 0, 18); root.addView(it) }
    private fun success(value: String) = text(value, 17, Color.rgb(24, 120, 78)).also { it.setPadding(0, 18, 0, 8); root.addView(it) }
    private fun toastText(value: String) { android.widget.Toast.makeText(this, value, android.widget.Toast.LENGTH_LONG).show() }
    private fun modeButton(label: String, detail: String, action: () -> Unit) { button(label, action = action); paragraph(detail, muted = true) }

    private fun button(label: String, enabled: Boolean = true, action: () -> Unit): Button = Button(this).apply {
        text = label; isAllCaps = false; textSize = 17f; isEnabled = enabled
        contentDescription = label
        setOnClickListener { action() }
        layoutParams = LinearLayout.LayoutParams(-1, -2).also { it.setMargins(0, 8, 0, 8) }
        root.addView(this)
    }

    private fun text(value: String, size: Int, color: Int) = TextView(this).apply {
        text = value; textSize = size.toFloat(); setTextColor(color); gravity = Gravity.CENTER
        importantForAccessibility = View.IMPORTANT_FOR_ACCESSIBILITY_YES
    }
}
