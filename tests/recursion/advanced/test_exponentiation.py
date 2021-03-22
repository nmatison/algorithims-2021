from pytest import mark
from algorithims.other.recursion.advanced.exponentiation import exponentiation_1, exponentiation_2


@mark.parametrize(
    'description, base, exponent, expected',
    [
        ('It handles 0', 0, 10, 0),
        ('It handles 1', 1, 555, 1),
        ('It handles a positive base with a positive exponent', 4, 5, 1024),
        ('It handles a negative base with a positive exponent and a positive return', -8, 4, 4096),
        ('It handles a negative base with a positive exponent and a negative return', -17, 5, -1419857),
        ('It handles a positive base with a negative exponent', 2, -3, 0.125),
        ('It handles a negative base with a negative exponent', -2, -3, -0.125),
    ]
)
class TestExponentiation:
    def test__exponentiation_1(self, description: str, base: int, exponent: int, expected: int) -> None:
        assert expected == exponentiation_1(base, exponent)
