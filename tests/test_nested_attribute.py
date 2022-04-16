import pytest

from dependencies.attribute_widget import NestedAttributeWidget


@pytest.fixture
def setup() -> None:
    widget = NestedAttributeWidget("main", {"sub1": "value", "sub2": "value"})
    yield widget


def test_nested_attribute_widget(setup, qtbot):
    widget = setup
    for target, attribute in zip([("sub1", "value"), ("sub2", "value")], widget.attributes):
        key = target[0]
        value = target[1]
        assert attribute.key == key
        assert attribute._value == value


def test_get(setup, qtbot):
    widget: NestedAttributeWidget = setup
    key, value = widget.get()
    assert {key: value} == {"main": {"sub1": "value", "sub2": "value"}}


def test_nested_get(setup, qtbot):
    widget = NestedAttributeWidget("main", {"sub": {"sub1": "value", "sub2": "value"}})
    key, value = widget.get()
    assert {key: value} == {"main": {"sub": {"sub1": "value", "sub2": "value"}}}
