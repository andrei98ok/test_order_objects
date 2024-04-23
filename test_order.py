import pytest
from order_objects import order_objects_by_color

def test_order_objects_by_color():
    input_objects = "ССЗСКЗЗЗККСЗССКЗ"
    expected_output = ["З", "З", "З", "З", "З", "З", "С", "С", "С", "С", "С", "С", "К", "К", "К", "К"]

    output_objects = order_objects_by_color(list(input_objects))

    assert output_objects == expected_output