from PyQt5 import QtCore

from dependencies.attribute_widget import AttributeWidget
from tests.aux import _setup


def test_attribute_w_value(qtbot):
    attribute_widget = AttributeWidget("key", "value")
    assert attribute_widget is not None


def test_attribute_wo_value(qtbot):
    attribute_widget = AttributeWidget("key", "")
    assert attribute_widget is not None


def test_attribute_set(qtbot):
    attribute_widget = AttributeWidget("key", "value")
    attribute_widget.set("new_value")
    assert attribute_widget.value == "new_value"


def test_attribute_get(qtbot):
    attribute_widget = AttributeWidget("key", "value")
    key, value = attribute_widget.get()
    assert key == "key"
    assert value == "value"


def test_update_existing_entry(qtbot):
    bg = _setup(qtbot)
    bg.file_selector.input_line.setText("tests/json/attribute.json")
    bg.file_selector.emit_update_file()
    qtbot.mouseClick(bg.existing_entry_widget.update_button, QtCore.Qt.LeftButton)
