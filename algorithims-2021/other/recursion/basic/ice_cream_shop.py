from typing import List

"""
Write a function ice_cream_shop(flavors, favorite) that takes in an array of ice cream flavors available at the ice cream shop, as well as the user's favorite ice cream flavor. Recursively find out whether or not the shop offers their favorite flavor.

  # Test Cases
  ice_cream_shop(['vanilla', 'strawberry'], 'blue moon')  # => returns false
  ice_cream_shop(['pistachio', 'green tea', 'chocolate', 'mint chip'], 'green tea')  # => returns true
  ice_cream_shop(['cookies n cream', 'blue moon', 'superman', 'honey lavender', 'sea salt caramel'], 'pistachio')  # => returns false
  ice_cream_shop(['moose tracks'], 'moose tracks')  # => returns true
  ice_cream_shop([], 'honey lavender')  # => returns false

"""


def ice_cream_shop(flavors: List[str], favorite: str) -> bool:
    if not flavors:
        return False

    if len(flavors) == 1:
        return flavors[0] == favorite

    if flavors[0] == favorite:
        return True

    return ice_cream_shop(flavors[1:], favorite)