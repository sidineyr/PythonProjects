package br.com.sidineyr.somente

import android.app.Activity
import com.google.android.gms.ads.AdRequest
import com.google.android.gms.ads.FullScreenContentCallback
import com.google.android.gms.ads.interstitial.InterstitialAd
import com.google.android.gms.ads.interstitial.InterstitialAdLoadCallback

class AdController(private val activity: Activity) {
    private var loaded: InterstitialAd? = null

    fun preload() {
        if (!BuildConfig.ADS_ENABLED || loaded != null) return
        InterstitialAd.load(activity, BuildConfig.ADMOB_INTERSTITIAL_ID, AdRequest.Builder().build(),
            object : InterstitialAdLoadCallback() {
                override fun onAdLoaded(ad: InterstitialAd) { loaded = ad }
            })
    }

    fun showIfReady(onClosed: () -> Unit): Boolean {
        val ad = loaded ?: return false
        loaded = null
        ad.fullScreenContentCallback = object : FullScreenContentCallback() {
            override fun onAdDismissedFullScreenContent() { onClosed(); preload() }
        }
        ad.show(activity)
        return true
    }
}
