from PyQt5.QtWidgets import QFrame, QLineEdit, QPushButton, QLabel, QVBoxLayout, QComboBox, QSizePolicy, QHBoxLayout
from dependencies.frames import LightFrame


class AttributeLabel(QLabel):
    pass


class AttributeLineEdit(QLineEdit):
    pass


class AttributeWidget(LightFrame):
    def __init__(self, key, value):
        super().__init__()
        self.key = key
        self._setup_ui(key, value)

    def _setup_ui(self, key, value):
        self.label = AttributeLabel(key)
        self.label.setFixedWidth(200)
        self.input_line = AttributeLineEdit()
        self.input_line.setText(str(value))
        self.setLayout(QHBoxLayout())
        self.layout().addWidget(self.label)
        self.layout().addWidget(self.input_line)

    @property
    def value(self):
        return self.input_line.text()

    def get(self):
        return self.key, self.value

    def set(self, value):
        self.input_line.setText(str(value))
