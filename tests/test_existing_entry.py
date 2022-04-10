from PyQt5 import QtCore

from tests.support_functions import _setup


def test_existing_entry_no_file(qtbot):
    bg = _setup(qtbot)
    bg.file_selector.input_line.setText("tests/json/attribute.json")
    bg.file_selector.emit_update_file()
    assert len(bg.existing_entry_widget.entry_frame.attribute_widgets) == 4


def test_update_existing_entry(qtbot):
    bg = _setup(qtbot)
    bg.file_selector.input_line.setText("tests/json/attribute.json")
    bg.file_selector.emit_update_file()
    qtbot.mouseClick(bg.existing_entry_widget.update_button, QtCore.Qt.LeftButton)
