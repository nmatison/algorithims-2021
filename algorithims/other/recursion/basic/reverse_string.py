"""
Write a function reverse(string) that takes in a string and returns it reversed.

  # Test Cases
  reverse("house") # => "esuoh"
  reverse("dog") # => "god"
  reverse("atom") # => "mota"
  reverse("q") # => "q"
  reverse("id") # => "di"
  reverse("") # => ""
"""

def reverse(s: str) -> str:
    if not s:
        return s

    return s[-1] + reverse(s[0:-1])