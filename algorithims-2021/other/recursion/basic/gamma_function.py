from typing import Optional

# Let's write a method that will solve Gamma Function recursively. The Gamma Function is defined Γ(n) = (n-1)!.
#
# # Test Cases
# gamma_fnc(0)  # => returns nil
# gamma_fnc(1)  # => returns 1
# gamma_fnc(4)  # => returns 6
# gamma_fnc(8)  # => returns 5040

def gamma_fnc(n: int) -> Optional[int]:
    if n == 0:
        return None
    if n == 1:
        return 1


    return gamma_fnc(n-1) * (n - 1)