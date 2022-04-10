from PyQt5.QtCore import QTimer, QPropertyAnimation
from PyQt5.QtWidgets import QStatusBar


class StatusBar(QStatusBar):
    ANIMATION_DURATION = 250
    MAX_HEIGHT = 75
    MIN_HEIGHT = 0

    def __init__(self, signal_nexus):
        super().__init__()
        self.setMaximumHeight(self.MIN_HEIGHT)
        self.signal_nexus = signal_nexus
        self.signal_nexus.status_bar_signal.connect(self.show_message)
        self.hide_animation = QPropertyAnimation(self, b"maximumHeight")
        self.hide_animation.setDuration(self.ANIMATION_DURATION)
        self.hide_animation.setStartValue(self.MAX_HEIGHT)
        self.hide_animation.setEndValue(self.MIN_HEIGHT)

        self.hide_timer = QTimer()
        self.hide_timer.timeout.connect(self.hide_animation.start)
        self.hide_timer.setSingleShot(True)

        self.show_animation = QPropertyAnimation(self, b"maximumHeight")
        self.show_animation.setDuration(0)
        self.show_animation.setStartValue(self.MIN_HEIGHT)
        self.show_animation.setEndValue(self.MAX_HEIGHT)

    def show_bar(self):
        self.show_animation.start()

    def show_message(self, message, timeout, color="red"):
        self.show_bar()
        self.showMessage(message, timeout+self.ANIMATION_DURATION)
        self.hide_timer.start(timeout)
