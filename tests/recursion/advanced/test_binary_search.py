from pytest import mark
from typing import List, Optional
from algorithims.other.recursion.advanced.binary_search import binary_search

class TestBinarySearch:
    @mark.parametrize(
        'description, nums, target, expected_index',
        [
            ('It handles an empty list', [], 3, None),
            ('It handles a basic test case', [1, 2, 3], 1, 0),
            ('It handles the value is in the middle', [2, 4, 6, 8, 10], 6, 2),
            ('It handles when the value is at the end', [1, 2, 3, 4, 5, 6], 6, 5),
            ('It handles when the value is at the end (longer)', [1, 2, 3, 4, 5, 6, 8, 20, 100, 150], 150, 9),
            ('It handles when the target does not appear', [1, 2, 3, 4, 5, 7], 6, None),
        ]
    )
    def test__binary_search(self, description: str, nums: List[int], target: int, expected_index: Optional[int]) -> None:

        assert binary_search(nums, target) == expected_index
