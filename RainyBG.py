import logging

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QApplication, QFrame, QVBoxLayout, QTabWidget, QSizePolicy, QStatusBar
from PyQt5.QtCore import pyqtSignal, QObject, QTimer, QPropertyAnimation
import os
import sys
from dependencies.existing_entry import ExistingEntryWidget
from dependencies.file_selector import FileSelector
from dependencies.new_entry import NewEntryWidget
from dependencies.status_bar import StatusBar
from dependencies.tab_bar import TabBar
from dependencies.template_selector import TemplateSelector


class SignalNexus(QObject):
    update_file_signal = pyqtSignal(str, name="update_file_signal")
    status_bar_signal = pyqtSignal(str, int, name="status_bar_signal")


class RainyBG(QMainWindow):
    signal_nexus = SignalNexus()

    def __init__(self, db_path, template_path="templates"):
        super().__init__()
        self.db_path = db_path
        self.template_path = template_path
        self._setup_ui()
        # self._setup_menu()
        self._bind_signals()
        self._display_ui()
        self.setStyleSheet(open(os.path.join("styles", "default.css")).read())

    def _setup_ui(self):
        # central frame
        self.window_frame = QFrame()
        self.window_frame.setLayout(QVBoxLayout())

        # file select
        self.file_selector = FileSelector(self.signal_nexus)

        # tab widget
        self.tab_widget = QTabWidget()
        self.tab_widget.setTabBar(TabBar(self.tab_widget))
        self.tab_widget.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)

        # entry widgets
        self.new_entry_widget = NewEntryWidget(self.signal_nexus, self.template_path)
        self.existing_entry_widget = ExistingEntryWidget(self.signal_nexus)

        self.setWindowTitle("RainyBG")
        self.setWindowIcon(QIcon(os.path.join("assets", "RainyBG2_icon.png")))
        self.resize(1300, 700)

        # status bar
        self.setStatusBar(StatusBar(self.signal_nexus))

    def _bind_signals(self):
        pass

    def _display_ui(self):
        self.setCentralWidget(self.window_frame)
        self.window_frame.layout().addWidget(self.file_selector)
        self.window_frame.layout().addWidget(self.tab_widget)

        self.tab_widget.addTab(self.existing_entry_widget, "Edit entries")
        self.tab_widget.addTab(self.new_entry_widget, "New entry")


def setup_logger():
    logging.basicConfig(
        format="%(asctime)-5s %(levelname)10s %(message)s",
        datefmt="%d-%m-%Y_%H_%M",
        level=logging.DEBUG,
        filemode='w'
    )


def open_rainy_bag(db_path, template_path):
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    form = RainyBG(
        db_path=db_path,
        template_path=template_path
    )
    setup_logger()

    form.show()  # Show the form
    sys.exit(app.exec_())  # and execute the app


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='RainyBG')
    parser.add_argument('--db', type=str, default='RainyDB', help='Path to the database')
    parser.add_argument('--template', type=str, default='templates', help='Path to the templates')
    args = parser.parse_args()
    open_rainy_bag(args.db, args.template)
