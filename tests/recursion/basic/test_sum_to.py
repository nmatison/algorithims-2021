from typing import Optional
from pytest import mark
from algorithims.other.recursion.basic.sum_to import sum_to


@mark.parametrize(
    'description, num, expected',
    [
        ('It handles one', 1, 1),
        ('It handles a number larger than one', 9, 45),
        ('It handles a number less than one', -10, None),
    ]
)
class TestSumTo:
    def test__sum_to(self, description: str, num: int, expected: Optional[int]) -> None:
        assert expected == sum_to(num)
