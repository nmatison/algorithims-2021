from typing import List, Optional

"""
Write a function add_numbers(nums_array) that takes in an array of Integers and returns the sum of those numbers. Write this method recursively.

  # Test Cases
  add_numbers([1,2,3,4]) # => returns 10
  add_numbers([3]) # => returns 3
  add_numbers([-80,34,7]) # => returns -39
  add_numbers([]) # => returns nil
"""


def add_numbers(nums: List[int]) -> Optional[int]:
    if not nums:
        return None

    if len(nums) == 1:
        return nums[0]

    return add_numbers(nums[1:]) + nums[0]