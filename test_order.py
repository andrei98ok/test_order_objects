import pytest
from order_objects import order_objects_by_color

def test_id9():
    input_objects = "ССЗСКЗЗЗККСЗССКЗ"
    expected_output = ["З", "З", "З", "З", "З", "З", "С", "С", "С", "С", "С", "С", "К", "К", "К", "К"]

    output_objects = order_objects_by_color("".join(input_objects))

    assert output_objects == expected_output

def test_id2():
    input_objects = "С"
    expected_output = ["С"]

    output_objects = order_objects_by_color("".join(input_objects))

    assert output_objects == expected_output

def test_id8():
    input_objects = "ЗСКQAZ!23"
    expected_output = ["З","С","К"]

    output_objects = order_objects_by_color("".join(input_objects))

    assert output_objects == expected_output

def test_id6():
    input_objects = "QAZ"
    expected_output = []

    output_objects = order_objects_by_color("".join(input_objects))

    assert output_objects == expected_output