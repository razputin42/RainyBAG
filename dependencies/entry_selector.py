from PyQt5.QtWidgets import QHBoxLayout, QComboBox, QLabel
from dependencies.frames import LightFrame


class EntrySelector(LightFrame):
    def __init__(self):
        super().__init__()
        self._setup_ui()
        self._display_ui()

    def _setup_ui(self):
        self.setLayout(QHBoxLayout())
        self.dropdown = QComboBox()
        self.label = QLabel("Entry")

    def _display_ui(self):
        self.layout().addWidget(self.label)
        self.layout().addWidget(self.dropdown)

    def update_items(self, dictionaries: list[dict]):
        self.entries = dictionaries
        self.dropdown.clear()
        items = []
        for dictionary in dictionaries:
            name = dictionary.get("name")
            if name is not None:
                items.append(name)
        self.dropdown.addItems(items)
        self.dropdown.setCurrentIndex(0)

    def get_selected_entry(self):
        selected_entry = self.dropdown.currentText()
        entry = self.get_entry(selected_entry)
        return entry

    def get_entries(self):
        return self.entries

    def get_entry(self, value, key="name"):
        for entry in self.entries:
            if entry[key] == value:
                return entry
        return None
