from typing import Optional

"""
Write a function sum_to(n) that uses recursion to calculate the sum from 1 to n (inclusive of n).
"""

def sum_to(num: int) -> Optional[int]:
    if num < 1:
        return None

    if num == 1:
        return num

    return sum_to(num - 1) + num