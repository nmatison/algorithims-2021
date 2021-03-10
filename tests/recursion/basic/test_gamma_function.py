from typing import Optional
from pytest import mark
from algorithims.other.recursion.basic.gamma_function import gamma_fnc


@mark.parametrize(
    'description, num, expected',
    [
        ('Handles a value less than 1', 0, None),
        ('Handles a basic case', 4, 6),
        ('Handles a much larger case', 8, 5040),
    ]
)
class TestGammaFunction:
    def test__add_numbers(self, description: str, num: int, expected: Optional[int]) -> None:
        assert expected == gamma_fnc(num)