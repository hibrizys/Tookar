package com.example.barterapp.views

import androidx.appcompat.app.AppCompatActivity
import android.content.pm.ActivityInfo
import android.media.MediaPlayer
import android.net.Uri
import android.os.Bundle
import android.view.View
import android.widget.MediaController
import android.widget.ProgressBar
import android.widget.VideoView
import com.example.barterapp.R

/**
 * Digunakan untuk melihat video produk.
 */
class ViewVideoActivity : AppCompatActivity() {
    private var mVideoUri: String? = null
    private lateinit var mVideoView: VideoView
    private lateinit var mProgressBar: ProgressBar

    /**
     * Menginisialisasi anggota kelas
     *
     * @param savedInstanceState
     * @return Unit
     */
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_view_video)
        requestedOrientation = ActivityInfo.SCREEN_ORIENTATION_PORTRAIT

        mVideoUri = intent.getStringExtra(getString(R.string.view_video_info_tag))

        mVideoView = findViewById(R.id.vv_view_video)
        mProgressBar = findViewById(R.id.pb_view_video)

        val mediaController = MediaController(this)
        mediaController.setAnchorView(mVideoView)
        mVideoView.setMediaController(mediaController)

        if (!mVideoUri.isNullOrEmpty()) {
            val uri = Uri.parse(mVideoUri)
            mVideoView.setVideoURI(uri)
            mVideoView.start()

            mProgressBar.visibility = View.VISIBLE

            mVideoView.setOnPreparedListener { mp ->
                mp.start()
                mp.setOnVideoSizeChangedListener { mp, _, _ ->
                    mProgressBar.visibility = View.GONE
                    mp.start()
                }
            }
        }
    }
}
