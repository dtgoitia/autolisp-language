import pytest

from autolisp.parse import parse, DefineFunction, _convert_to_lists


def test_defun():
    lsp = "(defun foo() 1)"

    ast = parse(lsp)

    assert ast == DefineFunction(name="foo", body=[])


@pytest.mark.parametrize(
    ("tokens", "result"),
    (
        pytest.param(
            ("(", "a", "b", ")"),
            ["a", "b"],
            id="flat_list",
        ),
        # pytest.param("(", "a", "b", ")", id="flat_list"),
    ),
)
def test_conver_to_lists(tokens, result):
    breakpoint()
    assert _convert_to_lists(tokens) == result


# TODO: support inline comments
# TODO: support multiline comments