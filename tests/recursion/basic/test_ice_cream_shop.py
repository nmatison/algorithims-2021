from typing import List
from pytest import mark
from algorithims.other.recursion.basic.ice_cream_shop import ice_cream_shop


@mark.parametrize(
    'description, flavors, favorite, expected',
    [
        ('It handles when the favorite flavor does not exist', ['vanilla', 'strawberry'], 'blue moon', False),
        ('It handles when the favorite flavor does not exist (longer list)', ['cookies n cream', 'blue moon', 'superman', 'honey lavender', 'sea salt caramel'], 'pistachio', False),
        ('It handles when the favorite flavor is nested in the list', ['pistachio', 'green tea', 'chocolate', 'mint chip'], 'green tea', True),
        ('It handles when there is only a favorite flavor', ['moose tracks'], 'moose tracks', True),
        ('It handles an empty list', [], 'honey lavender', False),
    ]
)
class TestIceCreamShop:
    def test__ice_cream_shop(self, description: str, flavors: List[str], favorite: str, expected: bool) -> None:
        assert expected == ice_cream_shop(flavors, favorite)

