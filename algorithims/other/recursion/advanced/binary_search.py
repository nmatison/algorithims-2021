from typing import List, Optional
from math import floor


def binary_search(sorted_values: List[int], target: int) -> Optional[int]:
    if not sorted_values:
        return None

    middle_index: int = floor(len(sorted_values) / 2)

    middle_value: int = sorted_values[middle_index]

    if target == middle_value:
        return middle_index
    elif target < middle_value:
        left_value = binary_search(sorted_values[:middle_index], target)
        return left_value
    else:
        right_value = binary_search(sorted_values[middle_index + 1:], target)
        if right_value is not None:
            return middle_index + right_value + 1
        else:
            return right_value
