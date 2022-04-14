from PyQt5.QtWidgets import QFrame, QLineEdit, QLabel, QHBoxLayout, QVBoxLayout

from dependencies.frames import LightFrame


class AddAttributeFrame(QFrame):
    pass


class AttributeLabel(QLabel):
    pass


class AttributeLineEdit(QLineEdit):
    pass


class AttributeWidget(LightFrame):
    def __init__(self, key, value=""):
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
        self.setContentsMargins(0, 0, 0, 0)
        # self.layout().setContentsMargins(0, 0, 0, 0)

    @property
    def value(self):
        return self.input_line.text()

    def get(self):
        return self.key, self.value

    def set(self, value):
        self.input_line.setText(str(value))


class NestedAttributeWidget(LightFrame):
    def __init__(self, key, value):
        super().__init__()
        self.attributes = []
        self.key = key
        self._value = value
        self._setup_ui(key, value)

    def _setup_ui(self, key, value):
        self.label = AttributeLabel(key)
        self.label.setFixedWidth(200)
        self.setLayout(QVBoxLayout())
        self.layout().setContentsMargins(10, 0, 0, 0)
        self.layout().addWidget(self.label)
        for _key, _value in value.items():
            attribute_widget = attribute_factory(_key, _value)
            self.attributes.append(attribute_widget)
            self.layout().addWidget(attribute_widget)

    @property
    def value(self):
        return self.input_line.text()

    def get(self):
        return self.key, self.value

    def set(self, value):
        self.input_line.setText(str(value))


def attribute_factory(key, value):
    if isinstance(value, dict):
        return NestedAttributeWidget(key, value)
    else:
        return AttributeWidget(key, value)
