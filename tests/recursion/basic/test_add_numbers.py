from typing import List
from pytest import mark
from algorithims.other.recursion.basic.add_numbers import add_numbers


@mark.parametrize(
    'description, nums, expected',
    [
        ('It handles a single number', [3], 3),
        ('It handles multiple numbers', [1,2,3,4], 10),
        ('It handles negative numbers', [-80,34,7], -39),
        ('It handles an empty list', [], None),
    ]
)
class TestAddNumbers:
    def test__add_numbers(self, description: str, nums: List[int], expected: int) -> None:
        assert expected == add_numbers(nums)
