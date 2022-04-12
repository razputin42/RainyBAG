import logging

import ujson
from PyQt5.QtWidgets import QFrame, QPushButton, QVBoxLayout

from dependencies.entry_frame import EntryFrame
from dependencies.entry_selector import EntrySelector


class ExistingEntryWidget(QFrame):
    def __init__(self, signal_nexus):
        super().__init__()
        self.signal_nexus = signal_nexus
        self.entries = []
        self._setup_ui()
        self._display_ui()
        self._bind_signal()

    def _setup_ui(self):
        self.setLayout(QVBoxLayout())
        self.entry_selector = EntrySelector()
        self.entry_frame = EntryFrame()
        self.update_button = QPushButton("Update Entry")

    def _display_ui(self):
        self.layout().addWidget(self.entry_selector)
        self.layout().addWidget(self.entry_frame)
        self.layout().addWidget(self.update_button)

    def _bind_signal(self):
        self.signal_nexus.update_file_signal.connect(self.refresh_file)
        self.entry_selector.dropdown.currentIndexChanged.connect(self.refresh_attributes)
        self.update_button.clicked.connect(self.update_existing_entry)

    def refresh_file(self, filename):
        logging.debug(f"Updating existing entry to {filename}")
        try:
            with open(filename, 'r') as f:
                dictionaries_in_file = ujson.load(f)
                logging.debug(f"Found {dictionaries_in_file}")
                self.entries = dictionaries_in_file
                self.filename = filename
                self.entry_selector.update_items(dictionaries_in_file)
                if self.entry_frame.is_empty():
                    self.refresh_attributes()
        except FileNotFoundError:
            logging.debug(f"Could not locate file {filename}")
            self.signal_nexus.status_bar_signal.emit("File not found!", 2000)
            return

    def refresh_attributes(self):
        logging.debug("Updating entries")
        self.entry_frame.clear_fields()
        entry = self.entry_selector.get_selected_entry()
        self.entry_frame.add_fields(entry)

    def update_existing_entry(self):
        entry = self.entry_frame.get_fields()
        for itt, _entry in enumerate(self.entries):
            if _entry["name"] == entry["name"]:
                self.entries[itt] = entry
        with open(self.filename, 'w') as f:
            ujson.dump(self.entries, f, indent=4)
        self.signal_nexus.status_bar_signal.emit("Entry updated!", 2000)

