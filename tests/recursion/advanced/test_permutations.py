from typing import List, Any
from pytest import mark
from algorithims.other.recursion.advanced.permutations import permutations


class TestPermutations:
    @mark.parametrize(
        'description, elements, expected',
        [
            ('It handles an empty array', [], [[]]),
            ('It handles a single element', [1], [[1]]),
            ('It handles multiple elements', [1, 2, 3], [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]])
        ]
    )
    def test__permutations(self, description: str, elements: List[Any], expected: List[Any]) -> None:
        assert permutations(elements).sort() == expected.sort()
