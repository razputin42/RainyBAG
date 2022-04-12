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

    def set_current_index(self, index):
        self.dropdown.setCurrentIndex(index)

    def update_items(self, dictionaries: list[dict]):
        self.entries = dictionaries
        current_index = self.dropdown.currentIndex()
        self.dropdown.blockSignals(True)
        self.dropdown.clear()
        items = []
        for dictionary in dictionaries:
            name = dictionary.get("name")
            if name is not None:
                items.append(name)
        self.dropdown.addItems(items)
        if self.dropdown.itemText(0) == "":
            self.dropdown.removeItem(0)
        if current_index == -1 or current_index >= self.dropdown.count():
            current_index = 0
        self.dropdown.setCurrentIndex(current_index)
        self.dropdown.blockSignals(False)
        self.dropdown.currentIndexChanged.emit(current_index)

    def get_selected_entry(self):
        selected_entry = self.dropdown.currentText()
        entry = self.get_entry(selected_entry)
        return entry

    def get_entries(self):
        return self.entries

    def get_entry(self, value, key="name"):
        for entry in self.entries:
            if key in entry and entry[key] == value:
                return entry
        raise ValueError(f"No entry with \"{key}\" equal to \"{value}\" found")
