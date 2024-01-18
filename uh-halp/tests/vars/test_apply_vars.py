from uh_halp.vars import apply_vars

vars = {"key1": "value1", "key2": "value2"}


def test_apply_vars_string():
    assert apply_vars(vars, "{key1}") == "value1"
    assert apply_vars(vars, "1={key1}, 2={key2}") == "1=value1, 2=value2"
    assert apply_vars(vars, "1={key1}, 2={key1}") == "1=value1, 2=value1"


def test_apply_vars_list():
    assert apply_vars(vars, ["{key1}", "{key2}"]) == ["value1", "value2"]
    assert apply_vars(vars, ["1={key1}, 2={key2}", "{key1}"]) == [
        "1=value1, 2=value2",
        "value1",
    ]


def test_apply_vars_dict():
    assert apply_vars(vars, {"key1": "{key1}", "key2": "{key2}"}) == {
        "key1": "value1",
        "key2": "value2",
    }
    assert apply_vars(vars, {"key1": "1={key1}, 2={key2}", "key2": "{key1}"})


def test_apply_vars_other():
    assert apply_vars(vars, 1) == 1
    assert apply_vars(vars, 1.0) == 1.0
    assert apply_vars(vars, True) is True
    assert apply_vars(vars, None) is None


def test_apply_vars_nested():
    assert apply_vars(vars, {"key1": "{key1}", "key2": ["{key1}", "{key2}", True]}) == {
        "key1": "value1",
        "key2": ["value1", "value2", True],
    }
    assert apply_vars
