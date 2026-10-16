package br.com.sidineyr.somente

import android.content.Context
import android.graphics.Canvas
import android.graphics.Color
import android.graphics.Paint
import android.view.View
import kotlin.math.max

class StaffView(context: Context) : View(context) {
    var notes: List<MusicNote> = emptyList()
        set(value) { field = value; activeIndex = -1; invalidate() }
    var activeIndex = -1
        set(value) { field = value; invalidate() }

    private val line = Paint(Paint.ANTI_ALIAS_FLAG).apply { color = Color.rgb(62, 57, 91); strokeWidth = 3f }
    private val note = Paint(Paint.ANTI_ALIAS_FLAG).apply { color = Color.rgb(108, 92, 231) }
    private val active = Paint(Paint.ANTI_ALIAS_FLAG).apply { color = Color.rgb(247, 190, 55) }
    private val label = Paint(Paint.ANTI_ALIAS_FLAG).apply { color = Color.DKGRAY; textSize = 28f; textAlign = Paint.Align.CENTER }

    override fun onMeasure(widthMeasureSpec: Int, heightMeasureSpec: Int) {
        setMeasuredDimension(MeasureSpec.getSize(widthMeasureSpec), 420)
    }

    override fun onDraw(canvas: Canvas) {
        super.onDraw(canvas)
        val gap = 30f
        val top = 58f
        for (i in 0..4) canvas.drawLine(24f, top + i * gap, width - 24f, top + i * gap, line)
        if (notes.isEmpty()) {
            canvas.drawText("Escolha notas para vê-las na pauta", width / 2f, 245f, label)
            return
        }
        val spacing = max(58f, (width - 80f) / notes.size.coerceAtMost(8))
        notes.forEachIndexed { index, musicNote ->
            val x = 48f + (index % 8) * spacing
            val row = index / 8
            val y = top + 4 * gap - musicNote.staffStep * (gap / 2) + row * 145f
            canvas.drawOval(x - 14, y - 10, x + 14, y + 10, if (index == activeIndex) active else note)
            canvas.drawLine(x + 13, y, x + 13, y - 55, line)
            canvas.drawText(musicNote.name, x, y + 43, label)
        }
    }
}
