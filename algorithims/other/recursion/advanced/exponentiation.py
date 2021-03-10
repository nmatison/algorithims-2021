from typing import Union
# Write two versions of exponent that use two different recursions:
#
# # this is math not code
#
# # recursion 1
# exp(b, 0) = 1
# exp(b, n) = b * exp(b, n - 1)
#
# # recursion 2
# exp(b, 0) = 1
# exp(b, 1) = b
# exp(b, n) = exp(b, n / 2) ** 2             [for even n]
# exp(b, n) = b * (exp(b, (n - 1) / 2) ** 2) [for odd n]

def exponentiation_1(base: int, exponent: int) -> Union[int, float]:
    if base == 0:
        return 0
    if abs(base) == 1:
        return base
    if exponent == 1:
        return base
    if exponent == -1:
        return 1/base
    if exponent == 0:
        return 0
    if exponent < 0:
        return exponentiation_1(base, exponent + 1) / 2

    return base * exponentiation_1(base, exponent- 1)
#


def exponentiation_2(base: int, exponent: int) -> int:
    pass