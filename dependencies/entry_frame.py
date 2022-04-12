from PyQt5.QtWidgets import QFrame, QSizePolicy, QVBoxLayout

from dependencies.attribute_widget import AttributeWidget


class EntryFrame(QFrame):
    def __init__(self):
        super().__init__()
        self.attribute_widgets = []
        self.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        self.setLayout(QVBoxLayout())

    def clear_fields(self):
        while self.layout().count():
            item = self.layout().takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()
        self.attribute_widgets = []

    def add_fields(self, dictionary):
        for key, value in dictionary.items():
            attribute_widget = AttributeWidget(key, value)
            self.attribute_widgets.append(attribute_widget)
            self.layout().addWidget(attribute_widget)
        self.layout().addStretch(1)

    def get_fields(self):
        entries = {}
        for attribute in self.attribute_widgets:
            key, value = attribute.get()
            entries[key] = value
        return entries

    def get_field(self, key="name"):
        for attribute in self.attribute_widgets:
            _key, value = attribute.get()
            if _key == key:
                return value

    def set_field(self, key, value):
        attribute: AttributeWidget
        for attribute in self.attribute_widgets:
            _key, _value = attribute.get()
            if _key == key:
                attribute.set(value)
                break

    def is_empty(self):
        return len(self.attribute_widgets) == 0

