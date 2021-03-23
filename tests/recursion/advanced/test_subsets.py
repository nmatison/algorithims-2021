from typing import List, Any
from pytest import mark
from algorithims.other.recursion.advanced.subsets import subsets


class TestSubsets:
    @mark.parametrize(
        'description, elements, expected',
        [
            ('It handles an empty array', [], [[]]),
            ("It handles a single entry", [1], [[], [1]]),
            ("It handles an array with two values", [1, 2], [[], [1], [2], [1, 2]]),
            ('It handles an array with even more values', [1, 2, 3], [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]),
            ('It handles other data types', ['banana', (1, 2)], [[], ['banana'], [(1, 2)], ['banana', (1, 2)]])
        ]
    )
    def test__subsets(self, description: str, elements: List[Any], expected: List[Any]) -> None:
        assert subsets(elements) == expected

