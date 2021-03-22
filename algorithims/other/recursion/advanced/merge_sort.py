from typing import List, Callable, Optional


def default_callback(a: int, b: int) -> bool:
    return a < b


def merge_sort(nums: List[int], callback: Optional[Callable[[int, int], bool]]) -> List[int]:
    if len(nums) <= 1:
        return nums

    if not callback:
        callback = default_callback

    pivot = nums[0]
    left_side: List[int] = [num for num in nums[1:] if callback(num, pivot)]
    right_side: List[int] = [num for num in nums[1:] if not callback(num, pivot)]

    return merge_sort(left_side, callback) + [pivot] + merge_sort(right_side, callback)