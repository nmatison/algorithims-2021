from typing import Optional
from pytest import mark
from algorithims.other.recursion.basic.range import range


@mark.parametrize(
    'description, start, end, expected',
    [
        ('It handles no range', 4, 4, []),
        ('It handles a single range', 5, 6, [5]),
        ('It handles a wide range', 1, 10, [1, 2, 3, 4, 5, 6, 7, 8, 9]),
        ('If end < start, it returns an empty list', 7, 4, [])
    ]
)
class TestSumTo:
    def test__sum_to(self, description: str, start: int, end: int, expected: Optional[int]) -> None:
        assert expected == range(start, end)
