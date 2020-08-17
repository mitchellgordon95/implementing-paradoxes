from number import Number


class Rational(Number):

    def __init__(self, numerator: int, denominator: int):
        self.top = numerator
        self.bot = denominator

        assert self.bot != 0
        # Ensure denominators are always positive
        if self.bot < 0:
            self.bot = -self.bot
            self.top = -self.top

    # TODO: make comparisons more memory efficient by finding smaller LCM
    def __eq__(self, other):
        return self.top * other.bot == other.top * self.bot

    def __lt__(self, other):
        return self.top * other.bot < other.top * self.bot

    def __le__(self, other):
        return self.top * other.bot <= other.top * self.bot

    def __abs__(self):
        return Rational(- self.top if self.top < 0 else self.top, self.bot)

    def __add__(self, other):
        return Rational(self.top * other.bot + other.top * self.bot, self.bot * other.bot)

    def __mul__(self, other):
        return Rational(self.top * other.top, self.bot * other.bot)

    def __neg__(self):
        return Rational(-self.top, self.bot)

    def invert(self):
        return Rational(self.bot, self.top)

    def __pow__(self, exp):
        return Rational(self.top ** exp, self.bot ** exp)

Q = Rational
assert Q(1, 3) < Q(2, 3)
assert Q(2, 3) >= Q(1, 3)
assert Q(2, 3) * Q(-3, 4) == Q(-6, 12)
assert Q(2, 3) * Q(-3, 4) == Q(6, -12)
