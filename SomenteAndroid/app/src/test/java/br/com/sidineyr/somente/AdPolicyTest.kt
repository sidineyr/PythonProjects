package br.com.sidineyr.somente

import org.junit.Assert.assertFalse
import org.junit.Assert.assertTrue
import org.junit.Test

class AdPolicyTest {
    private val now = 1_000_000L

    @Test fun `never interrupts first session or audio`() {
        assertFalse(AdPolicy.canShowAfterLesson(AdState(4, 0, 0, true, false), now))
        assertFalse(AdPolicy.canShowAfterLesson(AdState(4, 0, 0, false, true), now))
    }

    @Test fun `only shows at fourth completion after cooldown`() {
        assertFalse(AdPolicy.canShowAfterLesson(AdState(3, 0, 0, false, false), now))
        assertTrue(AdPolicy.canShowAfterLesson(AdState(4, 0, 0, false, false), now))
    }

    @Test fun `respects cooldown and daily limit`() {
        assertFalse(AdPolicy.canShowAfterLesson(AdState(8, 0, now - 1_000, false, false), now))
        assertFalse(AdPolicy.canShowAfterLesson(AdState(8, 3, 0, false, false), now))
    }
}
