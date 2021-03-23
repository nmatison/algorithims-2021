from typing import List, Any

# ("It handles an array with two values", [1, 2], [[], [1], [2], [1, 2]]),
def subsets(elements: List[Any]) -> List[Any]:
    if not elements:
        return [[]]

    result: List[Any] = []

    previous_elements: List[Any] = subsets(elements[:-1])
    result += previous_elements
    for prev in previous_elements:
        concat_list = prev + [elements[-1]]
        result.append(concat_list)

    return result



