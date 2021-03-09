"""
Write a function sum_to(n) that uses recursion to calculate the sum from 1 to n (inclusive of n).
"""

# Test Cases
# sum_to(5)  # => returns 15
# sum_to(1)  # => returns 1
# sum_to(9)  # => returns 45
# sum_to(-8)  # => returns nil


def sum_to(num: int) -> int:
    if num < 1:
        return None

    if num == 1:
        return num

    return sum_to(num - 1) + num

print(sum_to(5))
print(sum_to(1))
print(sum_to(9))
print(sum_to(-8))