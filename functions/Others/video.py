#Import Libs

import sys
from pathlib import Path

import cv2
import numpy as np

from PySide6.QtCore import Qt, QUrl, QTimer
from PySide6.QtGui import QAction, QKeySequence, QFont
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QFileDialog,
    QVBoxLayout, QHBoxLayout, QPushButton, QLabel,
    QSlider, QSizePolicy, QStackedWidget
)
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtMultimediaWidgets import QVideoWidget


class PyPlayer(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("PyPlayer")
        self.resize(1100, 720)
        self.setMinimumSize(700, 450)

        self.is_seeking = False
        self.duration = 0

        # ASCII settings
        self.ascii_capture = None
        self.ascii_timer = QTimer(self)
        self.ascii_timer.timeout.connect(self.update_ascii_frame)
        self.ascii_chars = " .:-=+*#%@"
        self.ascii_mode = False

        # Media engine
        self.player = QMediaPlayer(self)
        self.audio = QAudioOutput(self)
        self.player.setAudioOutput(self.audio)
        self.audio.setVolume(0.7)

        self.create_interface()
        self.create_connections()
        self.create_shortcuts()
        self.apply_style()

    # ================= INTERFACE =================

    def create_interface(self):

        central = QWidget()
        self.setCentralWidget(central)

        main = QVBoxLayout(central)
        main.setContentsMargins(18, 15, 18, 15)
        main.setSpacing(12)

        # Header
        header = QHBoxLayout()

        logo = QLabel("▶ PyPlayer")
        logo.setObjectName("logo")

        self.file_label = QLabel("No video selected")

        open_btn = QPushButton("＋ Open Video")
        open_btn.clicked.connect(self.open_video)

        self.ascii_btn = QPushButton("ASCII Mode")
        self.ascii_btn.clicked.connect(self.toggle_ascii_mode)

        header.addWidget(logo)
        header.addStretch()
        header.addWidget(self.file_label)
        header.addWidget(open_btn)
        header.addWidget(self.ascii_btn)

        main.addLayout(header)

        # Video and ASCII display stack
        self.display_stack = QStackedWidget()

        self.video = QVideoWidget()
        self.video.setStyleSheet("background: black;")

        self.player.setVideoOutput(self.video)

        self.ascii_display = QLabel("ASCII MODE")
        self.ascii_display.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.ascii_display.setStyleSheet(
            "background: black; color: white;"
        )
        self.ascii_display.setFont(
            QFont("Courier New", 7)
        )
        self.ascii_display.setTextInteractionFlags(
            Qt.TextInteractionFlag.NoTextInteraction
        )

        self.display_stack.addWidget(self.video)
        self.display_stack.addWidget(self.ascii_display)

        main.addWidget(self.display_stack, 1)

        # Timeline
        timeline = QHBoxLayout()

        self.current_time = QLabel("00:00")
        self.seek_slider = QSlider(Qt.Orientation.Horizontal)
        self.seek_slider.setRange(0, 0)
        self.total_time = QLabel("00:00")

        timeline.addWidget(self.current_time)
        timeline.addWidget(self.seek_slider, 1)
        timeline.addWidget(self.total_time)

        main.addLayout(timeline)

        # Controls
        controls = QHBoxLayout()

        self.back_btn = QPushButton("⏪ 10s")
        self.play_btn = QPushButton("▶")
        self.play_btn.setObjectName("playButton")
        self.play_btn.setFixedSize(55, 45)

        self.forward_btn = QPushButton("10s ⏩")
        self.mute_btn = QPushButton("🔊")

        self.volume_slider = QSlider(Qt.Orientation.Horizontal)
        self.volume_slider.setRange(0, 100)
        self.volume_slider.setValue(70)
        self.volume_slider.setFixedWidth(110)

        self.fullscreen_btn = QPushButton("⛶ Fullscreen")

        controls.addWidget(self.back_btn)
        controls.addWidget(self.play_btn)
        controls.addWidget(self.forward_btn)

        controls.addStretch()

        controls.addWidget(self.mute_btn)
        controls.addWidget(self.volume_slider)
        controls.addWidget(self.fullscreen_btn)

        main.addLayout(controls)

        self.statusBar().showMessage("Ready")

    # ================= CONNECTIONS =================

    def create_connections(self):

        self.play_btn.clicked.connect(self.toggle_play)

        self.back_btn.clicked.connect(
            lambda: self.skip(-10000)
        )

        self.forward_btn.clicked.connect(
            lambda: self.skip(10000)
        )

        self.mute_btn.clicked.connect(self.toggle_mute)

        self.volume_slider.valueChanged.connect(
            self.change_volume
        )

        self.fullscreen_btn.clicked.connect(
            self.toggle_fullscreen
        )

        self.seek_slider.sliderPressed.connect(
            self.start_seeking
        )

        self.seek_slider.sliderReleased.connect(
            self.finish_seeking
        )

        self.player.positionChanged.connect(
            self.update_position
        )

        self.player.durationChanged.connect(
            self.update_duration
        )

        self.player.playbackStateChanged.connect(
            self.update_play_button
        )

        self.player.errorOccurred.connect(
            self.handle_error
        )

    # ================= SHORTCUTS =================

    def create_shortcuts(self):

        shortcuts = [
            ("Space", self.toggle_play),
            ("Left", lambda: self.skip(-5000)),
            ("Right", lambda: self.skip(5000)),
            ("F", self.toggle_fullscreen),
            ("Ctrl+O", self.open_video),
        ]

        for key, callback in shortcuts:

            action = QAction(self)
            action.setShortcut(QKeySequence(key))
            action.triggered.connect(callback)

            self.addAction(action)

    # ================= STYLE =================

    def apply_style(self):

        self.setStyleSheet("""
            QMainWindow {
                background: #111218;
            }

            QWidget {
                color: #eeeeF5;
                font-family: Segoe UI, Arial;
                font-size: 13px;
            }

            QLabel#logo {
                color: #9185ff;
                font-size: 23px;
                font-weight: bold;
            }

            QPushButton {
                background: #252733;
                color: white;
                border: none;
                border-radius: 8px;
                padding: 10px 15px;
            }

            QPushButton:hover {
                background: #383b4c;
            }

            QPushButton#playButton {
                background: #7868ee;
                font-size: 19px;
            }

            QSlider::groove:horizontal {
                height: 5px;
                background: #393b49;
            }

            QSlider::sub-page:horizontal {
                background: #8576ff;
            }

            QSlider::handle:horizontal {
                background: white;
                width: 13px;
                margin: -5px 0;
                border-radius: 6px;
            }

            QStatusBar {
                background: #171820;
                color: #9698a8;
            }
        """)

    # ================= OPEN VIDEO =================

    def open_video(self):

        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Open Video",
            str(Path.home()),
            "Video Files (*.mp4 *.mkv *.avi *.mov *.wmv *.webm *.m4v)"
        )

        if file_path:
            self.open_video_instantly(file_path)

    def open_video_instantly(self, file_path, autoplay=True):

        path = Path(file_path).expanduser().resolve()

        if not path.is_file():
            self.statusBar().showMessage(
                f"File not found: {path}"
            )
            return False

        self.stop_ascii_video()

        self.ascii_mode = False
        self.display_stack.setCurrentWidget(self.video)

        self.player.setSource(
            QUrl.fromLocalFile(str(path))
        )

        self.file_label.setText(path.name)

        if autoplay:
            self.player.play()

        self.statusBar().showMessage(
            f"Loaded: {path.name}"
        )

        return True

    # ================= PLAYBACK =================

    def toggle_play(self):

        if self.player.source().isEmpty():
            self.open_video()
            return

        if self.player.playbackState() == (
            QMediaPlayer.PlaybackState.PlayingState
        ):
            self.player.pause()
        else:
            self.player.play()

    def update_play_button(self, state):

        if state == QMediaPlayer.PlaybackState.PlayingState:
            self.play_btn.setText("Ⅱ")
        else:
            self.play_btn.setText("▶")

    def skip(self, milliseconds):

        new_position = max(
            0,
            min(
                self.player.position() + milliseconds,
                self.duration
            )
        )

        self.player.setPosition(new_position)

    # ================= TIMELINE =================

    def start_seeking(self):
        self.is_seeking = True

    def finish_seeking(self):

        self.player.setPosition(
            self.seek_slider.value()
        )

        self.is_seeking = False

    def update_position(self, position):

        if not self.is_seeking:
            self.seek_slider.setValue(position)

        self.current_time.setText(
            self.format_time(position)
        )

    def update_duration(self, duration):

        self.duration = duration
        self.seek_slider.setRange(0, duration)

        self.total_time.setText(
            self.format_time(duration)
        )

    @staticmethod
    def format_time(milliseconds):

        seconds = milliseconds // 1000

        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        seconds = seconds % 60

        if hours:
            return f"{hours:02}:{minutes:02}:{seconds:02}"

        return f"{minutes:02}:{seconds:02}"

    # ================= VOLUME =================

    def change_volume(self, value):
        self.audio.setVolume(value / 100)

    def toggle_mute(self):

        muted = not self.audio.isMuted()
        self.audio.setMuted(muted)

        self.mute_btn.setText(
            "🔇" if muted else "🔊"
        )

    # ================= ASCII VIDEO =================

    def start_ascii_video(self, file_path, width=100):

        path = Path(file_path).expanduser().resolve()

        if not path.is_file():
            self.statusBar().showMessage("ASCII video not found")
            return False

        self.stop_ascii_video()

        self.ascii_capture = cv2.VideoCapture(str(path))

        if not self.ascii_capture.isOpened():
            self.ascii_capture.release()
            self.ascii_capture = None
            self.statusBar().showMessage("Cannot open ASCII video")
            return False

        self.ascii_width = max(20, min(width, 200))

        fps = self.ascii_capture.get(cv2.CAP_PROP_FPS)

        if not np.isfinite(fps) or fps <= 0:
            fps = 24

        self.ascii_timer.start(
            max(1, int(1000 / fps))
        )

        self.ascii_mode = True
        self.display_stack.setCurrentWidget(self.ascii_display)

        self.file_label.setText(path.name)
        self.statusBar().showMessage("ASCII playback")

        return True

    def update_ascii_frame(self):

        if self.ascii_capture is None:
            return

        success, frame = self.ascii_capture.read()

        if not success:
            self.stop_ascii_video()
            self.statusBar().showMessage("ASCII playback finished")
            return

        height, width = frame.shape[:2]

        if width == 0:
            return

        new_height = max(
            1,
            int(height * self.ascii_width / width * 0.5)
        )

        frame = cv2.resize(
            frame,
            (self.ascii_width, new_height)
        )

        gray = cv2.cvtColor(
            frame,
            cv2.COLOR_BGR2GRAY
        )

        indices = (
            gray.astype(np.int32) * (len(self.ascii_chars) - 1) // 255
        ).astype(np.int32)

        lines = [
            "".join(
                self.ascii_chars[index]
                for index in row
            )
            for row in indices
        ]

        self.ascii_display.setText("\n".join(lines))

    def stop_ascii_video(self):

        self.ascii_timer.stop()

        if self.ascii_capture is not None:
            self.ascii_capture.release()
            self.ascii_capture = None

    def toggle_ascii_mode(self):

        if self.ascii_mode:

            self.stop_ascii_video()
            self.ascii_mode = False

            self.display_stack.setCurrentWidget(self.video)
            self.ascii_btn.setText("ASCII Mode")

            return

        source = self.player.source()

        if source.isEmpty():
            self.open_video()
            return

        file_path = source.toLocalFile()

        if self.start_ascii_video(file_path):
            self.ascii_btn.setText("Normal Video")

    # ================= FULLSCREEN =================

    def toggle_fullscreen(self):

        if self.isFullScreen():
            self.showNormal()
            self.fullscreen_btn.setText("⛶ Fullscreen")
        else:
            self.showFullScreen()
            self.fullscreen_btn.setText("⛶ Exit Fullscreen")

    # ================= ERRORS =================

    def handle_error(self, error, message):

        if error != QMediaPlayer.Error.NoError:
            self.statusBar().showMessage(
                f"Playback error: {message}"
            )

    # ================= CLOSE =================

    def closeEvent(self, event):

        self.stop_ascii_video()
        self.player.stop()

        event.accept()


# ================= PUBLIC API =================

_player_instance = None


def start(file=None):

    global _player_instance

    app = QApplication.instance()

    if app is None:
        app = QApplication(sys.argv)

    _player_instance = PyPlayer()
    _player_instance.show()

    if file:
        _player_instance.open_video_instantly(file)

    return app.exec()


def play(file):

    return start(file)


def play_ascii(file, width=100):

    global _player_instance

    app = QApplication.instance()

    if app is None:
        app = QApplication(sys.argv)

    _player_instance = PyPlayer()
    _player_instance.show()

    _player_instance.start_ascii_video(file, width)

    return app.exec()


if __name__ == "__main__":
    start()
