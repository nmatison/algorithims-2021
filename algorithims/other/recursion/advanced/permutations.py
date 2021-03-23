from typing import List, Any

# ('It handles multiple elements', [1, 2, 3], [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]])

def permutations(elements: List[Any]) -> List[Any]:
    if not elements:
        return [[]]

    j: int = len(elements) - 1
    result: List[Any] = []
    while j >= 0:
        previous_permutation: List[Any] = permutations(elements[:j]+elements[j+1:])

        for permutation in previous_permutation:
            permutation.append(elements[j])
            result.append(permutation)

        j -= 1
    return result






#123 -> [[1, 2, 3], [2, 1, 3], [1, 3, 2], [3, 1, 2], [2, 3, 1], [3, 2, 1]]
#12 -> [[1, 2], [2, 1]] # 13 -> [[1, 3], [[3, 1]] # 23 -> [[2, 3], [3, 2]]
#1 -> [[1]]             # 1 -> [[1]]              # 2 -> [[2]]
