import os

from tests.support_functions import _setup
from PyQt5 import QtCore


def test_new_entry_set_template(qtbot):
    bg = _setup(qtbot)
    bg.file_selector.text_input.setText("tests/json/attribute.json")
    bg.file_selector.emit_update_file()
    bg.new_entry_widget.template_selector.dropdown.setCurrentIndex(0)
    attributes = bg.new_entry_widget.entry_frame.get_fields()
    assert attributes["name"] == ""

def test_new_entry_no_selection(qtbot):
    bg = _setup(qtbot)
    bg.tab_widget.setCurrentIndex(1)
    bg.file_selector.text_input.setText("tests/json/attribute.json")
    bg.file_selector.emit_update_file()
    attributes = bg.new_entry_widget.entry_frame.get_fields()
    assert attributes["name"] == ""

def test_new_entry_no_file(qtbot):
    bg = _setup(qtbot)
    bg.tab_widget.setCurrentIndex(1)
    attributes = bg.new_entry_widget.entry_frame.get_fields()
    assert attributes["name"] == ""

def test_add_entry_to_file_missing_name(qtbot):
    bg = _setup(qtbot)
    if os.path.exists("tests/json/test_attribute.json"):
        os.remove("tests/json/test_attribute.json")
    bg.file_selector.text_input.setText("tests/json/test_attribute.json")
    qtbot.mouseClick(bg.new_entry_widget.add_button, QtCore.Qt.LeftButton)
    assert not os.path.exists("tests/json/test_attribute.json")

def test_add_entry_to_file(qtbot):
    bg = _setup(qtbot)
    if os.path.exists("tests/json/test_attribute.json"):
        os.remove("tests/json/test_attribute.json")
    bg.file_selector.text_input.setText("tests/json/test_attribute.json")
    bg.file_selector.emit_update_file()
    bg.new_entry_widget.entry_frame.set_field("name", "Test")
    qtbot.mouseClick(bg.new_entry_widget.add_button, QtCore.Qt.LeftButton)
    assert os.path.exists("tests/json/test_attribute.json")

def test_adding_new_area(qtbot):
    bg = _setup(qtbot)
    bg.tab_widget.setCurrentIndex(1)
    bg.file_selector.text_input.setText("tests/json/attribute.json")
    bg.file_selector.emit_update_file()
    bg.new_entry_widget.template_selector.dropdown.setCurrentText("Area")
    bg.new_entry_widget.entry_frame.set_field("name", "Test")
    qtbot.mouseClick(bg.new_entry_widget.add_button, QtCore.Qt.LeftButton)
    # assert os.path.exists("tests/json/test_attribute.json")
