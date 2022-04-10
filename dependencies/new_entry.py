import os

import ujson
from PyQt5.QtWidgets import QFrame, QPushButton, QVBoxLayout

from dependencies.entry_frame import EntryFrame
from dependencies.template_selector import TemplateSelector


class NewEntryWidget(QFrame):
    def __init__(self, signal_nexus, template_path):
        super().__init__()
        self.signal_nexus = signal_nexus
        self.template_path = template_path
        self.filename = ""
        self._setup_ui()
        self._connect_signals()
        self._display_ui()

    def _setup_ui(self):
        self.setLayout(QVBoxLayout())
        self.template_selector = TemplateSelector(self.template_path)
        self.entry_frame = EntryFrame()
        self.add_button = QPushButton("Add Entry to File")
        self.layout().setSpacing(0)

    def _connect_signals(self):
        self.template_selector.dropdown.currentIndexChanged.connect(self._update_template)
        self.add_button.clicked.connect(self.add_entry_to_file)
        self.signal_nexus.update_file_signal.connect(self.refresh_file)

    def _display_ui(self):
        self.layout().addWidget(self.template_selector)
        self.layout().addWidget(self.entry_frame)
        self.layout().addWidget(self.add_button)
        self._update_template()

    def refresh_file(self, filename):
        self.filename = filename

    def _update_template(self):
        template = self.template_selector.get_selected_template()
        self.entry_frame.clear_fields()
        self.entry_frame.add_fields(template)

    def add_entry_to_file(self):
        if self.filename == "":
            self.signal_nexus.status_bar_signal.emit("No file selected!", 2000)
            return

        if os.path.exists(self.filename):
            with(open(self.filename, "r")) as file:
                entries = ujson.load(file)
        else:
            entries = []

        entry = self.entry_frame.get_fields()
        if "name" not in entry or entry["name"] == "":
            self.signal_nexus.status_bar_signal.emit("Attributes and templates must have a \"name\"!", 2000)
            return
        entries.append(entry)
        with(open(self.filename, "w")) as file:
            ujson.dump(entries, file, indent=4)
        self.signal_nexus.status_bar_signal.emit("Entry updated!", 2000)

