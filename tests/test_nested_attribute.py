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
        assert attribute.value == value

