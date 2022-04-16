from PyQt5.QtWidgets import QFrame, QLineEdit, QLabel, QHBoxLayout, QVBoxLayout, QPushButton

from dependencies.frames import LightFrame


class AddAttributeFrame(QFrame):
    pass


class AttributeLabel(QLabel):
    pass


class AttributeLineEdit(QLineEdit):
    pass


class BaseAttributeWidget(LightFrame):
    def __init__(self, key, value=""):
        super().__init__()
        self.key = key
        self._value = value
        self._setup_ui(key, value)

    def _setup_ui(self, key, value):
        raise NotImplementedError

    def get(self):
        raise NotImplementedError


class AttributeWidget(BaseAttributeWidget):
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


class NestedAttributeWidget(BaseAttributeWidget):
    attributes = []

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

    def get(self):
        return_dict = {}
        for attribute in self.attributes:
            key, value = attribute.get()
            return_dict[key] = value
        return self.key, return_dict


class ListAttributeWidget(BaseAttributeWidget):
    attributes = []

    def _setup_ui(self, key, value):
        self.attribute_frame = LightFrame()
        self.attribute_frame.setLayout(QVBoxLayout())
        for item in value:
            self.add_attribute(item)
        label = AttributeLabel(key)
        add_attribute_button = QPushButton("+")
        add_attribute_button.clicked.connect(self.add_attribute)
        self.setLayout(QVBoxLayout())
        self.layout().setContentsMargins(10, 0, 0, 0)
        self.layout().addWidget(label)
        self.layout().addWidget(self.attribute_frame)
        self.layout().addWidget(add_attribute_button)

    def add_attribute(self, value=None):
        if value is None or isinstance(value, list):
            value = ""
        new_attribute = attribute_factory(self.key, value)
        self.attributes.append(new_attribute)
        self.attribute_frame.layout().addWidget(new_attribute)

    def get(self):
        return_list = []
        for attribute in self.attributes:
            key, value = attribute.get()
            return_list.append(value)
        return self.key, return_list

    def set(self, value):
        print(value)


def attribute_factory(key, value):
    if isinstance(value, dict):
        return NestedAttributeWidget(key, value)
    elif isinstance(value, list):
        return ListAttributeWidget(key, value)
    else:
        return AttributeWidget(key, value)
