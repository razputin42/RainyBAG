import pytest

from dependencies.attribute_widget import ListAttributeWidget


@pytest.fixture
def setup() -> None:
    widget = ListAttributeWidget("main", [])
    yield widget


def test_nested_attribute_widget(setup, qtbot):
    widget = setup
    assert widget is not None


def test_get(setup, qtbot):
    widget = setup
    assert widget.get() == ("main", [])


def test_add_attribute(setup, qtbot):
    widget = setup
    widget.add_attribute()
    assert widget.get() == ("main", [""])


def test_add_attribute(setup, qtbot):
    widget = setup
    for i in range(3):
        widget.add_attribute()
    assert widget.get() == ("main", ["", "", ""])
