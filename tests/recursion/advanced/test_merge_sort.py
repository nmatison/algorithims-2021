from algorithims.other.recursion.advanced.merge_sort import merge_sort
from pytest import mark
from typing import List, Callable, Optional


class TestMergeSort:
    @mark.parametrize(
        'description, nums, callback, expected',
        [
            ('It handles an empty list', [], None, []),
            ('It handles a single value', [1], None, [1]),
            ('It handles a multiple of the same value', [1, 1, 1], None, [1, 1, 1]),
            ('It handles multiple values', [5, 3, 7, 10, 2, 22], None, [2, 3, 5, 7, 10, 22]),
            ('It handles even more values', [5, 3, 7, 10, 2, 22, 3, 1], None, [1, 2, 3, 3, 5, 7, 10, 22]),
            ('It handles multiple values with a callback', [5, 3, 7, 10, 2, 7, 22], lambda a, b: a > b, [22, 10, 7, 7, 5, 3, 2])

        ]
    )
    def test__merge_sort(self, description: str, nums: List[int], callback: Optional[Callable[[int, int], bool]], expected: List[int]) -> None:
        assert merge_sort(nums, callback) == expected
