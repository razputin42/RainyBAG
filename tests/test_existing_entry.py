from PyQt5 import QtCore

from tests.support_functions import _setup


def test_existing_entry_no_file(qtbot):
    bg = _setup(qtbot)
    bg.file_selector.text_input.setText("tests/json/attribute.json")
    bg.file_selector.emit_update_file()
    assert len(bg.existing_entry_widget.entry_frame.attribute_widgets) == 4


def test_update_existing_entry(qtbot):
    bg = _setup(qtbot)
    bg.file_selector.text_input.setText("tests/json/attribute.json")
    bg.file_selector.emit_update_file()
    qtbot.mouseClick(bg.existing_entry_widget.update_button, QtCore.Qt.LeftButton)


def test_switching_to_fewer_entries(qtbot):
    bg = _setup(qtbot)
    bg.file_selector.text_input.setText("tests/json/attribute.json")
    bg.file_selector.emit_update_file()
    bg.existing_entry_widget.entry_selector.set_current_index(2)
    bg.file_selector.text_input.setText("tests/json/site.json")
    bg.file_selector.emit_update_file()


def test_update_existing_entries_dropdown(qtbot):
    """
    Update the selected file, to show that the dropdown is properly updated
    """
    bg = _setup(qtbot)
    bg.file_selector.text_input.setText("tests/json/attribute.json")
    bg.file_selector.emit_update_file()
    bg.file_selector.text_input.setText("tests/json/resource.json")
    bg.file_selector.emit_update_file()
