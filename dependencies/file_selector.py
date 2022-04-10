import logging

from PyQt5.QtWidgets import QFrame, QLineEdit, QPushButton, QLabel, QHBoxLayout, QFileDialog


class FileSelector(QFrame):
    def __init__(self, signal_nexus):
        super().__init__()
        self.signal_nexus = signal_nexus
        self._setup_ui()
        self._display_ui()
        self._bind_signals()

    def _setup_ui(self):
        self.setLayout(QHBoxLayout())
        self.update_button = QPushButton("Update")
        self.file_dialog = QPushButton("Select File")
        self.input_line = QLineEdit()

    def _display_ui(self):
        self.layout().addWidget(self.input_line)
        self.layout().addWidget(self.file_dialog)
        self.layout().addWidget(self.update_button)

    def _bind_signals(self):
        self.update_button.clicked.connect(self.emit_update_file)
        self.file_dialog.clicked.connect(self.file_select_dialog)

    def emit_update_file(self, file=None):
        if file is None:
            file = self.input_line.text()
        logging.debug(f"Emitting update_file_signal with {file}")
        self.signal_nexus.update_file_signal.emit(file)

    def file_select_dialog(self):
        logging.debug("Opening QFileDialog")
        filename, active_filter = QFileDialog.getOpenFileName(self, "Select json", filter="*.json *.txt")
        logging.debug(f"Selected file: {filename}")
        self.input_line.setText(filename)
        self.emit_update_file(filename)
