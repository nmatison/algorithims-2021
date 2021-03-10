from pytest import mark
from algorithims.other.recursion.basic.reverse_string import reverse


@mark.parametrize(
    'description, s, expected',
    [
        ('It handles a single letter', 'q', 'q'),
        ('It handles an empty string', '', ''),
        ('It handles a word', 'ball', 'llab'),
        ('It handles multiple words', 'the Ball is Red', 'deR si llaB eht'),
        ('It handles nonsense symbols and characters', '1@!3$%^&7689)*(+-%4', '4%-+(*)9867&^%$3!@1'),
    ]
)
class TestSumTo:
    def test__reverse_string(self, description: str, s: str, expected: str) -> None:
        assert expected == reverse(s)
