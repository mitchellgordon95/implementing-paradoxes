from number import Number
from rationals import Q
from abc import ABC


class Interval(ABC):
    def bounds(self):
        pass


class RationalInverval:

    def __init__(self, val: Q):
        self.val = val

    def bounds(self, precision=None):
        return (self.val, self.val)


class InverseFunctionInterval:

    def __init__(self, fn, val: Q):
        self.fn = fn
        self.val = val

    def bounds(self, precision=Q(1,100000)):
        # TODO: Read the inverse function chapter
        pass


class Real(Number):

    # A real number is just an interval with variable precision.
    # If this real number is the result of an operation on one or more other real numbers,
    # we keep a reference to those numbers to get the appropriate precision when evaluating.
    def __init__(self, interval=None, fn=None):
        self._interval = interval
        self._fn = fn
        if self._interval:
            assert not fn

    def bounds(self, precision):
        if self._interval:
            return self._interval.bounds(precision)
        else:
            return self._fn(precision)

    def eq(self, other, precision):
        self_lb, self_ub = self.bounds(precision)
        other_lb, other_ub = other.bounds(precision)

        return self_ub >= other_lb and self_lb <= other_ub

    def lt(self, other, precision):
        _, self_ub = self.bounds(precision)
        other_lb, _ = other.bounds(precision)
        return self_ub < other_lb

    def le(self, other, precision):
        self_lb, _ = self.bounds(precision)
        _, other_ub = other.bounds(precision)
        return self_lb <= other_ub

    def __eq__(self, other):
        return self.eq(other, Q(1,1000000))

    def __lt__(self, other):
        return self.lt(other, Q(1,1000000))

    def __le__(self, other):
        return self.le(other, Q(1,1000000))

    def __abs__(self):

        def _abs(precision):
            lb, ub = self.bounds(precision)
            return (min(abs(lb), abs(ub)), max(abs(lb), abs(ub)))

        return Real(None, _abs)

    def __add__(self, other):

        def _add(precision):
            llb, lub = self.bounds(precision / 2)
            rlb, rub = other.bounds(precision / 2)
            return (llb + rlb, lub + rub)

        return Real(None, _add)

    def __mul__(self, other):

        def _mul(precision):
            tmp_llb, tmp_lub = self.bounds(precision)
            tmp_rlb, tmp_rub = other.bounds(precision)

            max_left = max(-tmp_llb, tmp_lub)
            max_right = max(-tmp_rlb, tmp_rub)

            llb, lub = self.bounds((precision / Q(2,1)) / max_left)
            rlb, rub = other.bounds((precision / Q(2,1)) / max_right)

            candidates = [llb * rlb, llb * rub, lub * rlb, lub * rub]
            return (min(candidates), max(candidates))

        return Real(None, _mul)

    def __neg__(self):

        def _neg(precision):
            lb, ub = self.bounds(precision)
            return (-ub, -lb)

        return Real(None, _neg)

    def invert(self):

        def _invert(precision):
            tmp_lb, tmp_ub = self.bounds(precision)
            if tmp_ub > 0:
                assert tmp_lb > 0, "Attempting to invert possibly 0 parent. Try increasing precision before inverting."
                precision = precision * (tmp_lb ** 2)
            else:
                assert tmp_lb < 0, "Lower bound greater than upper bound?"
                precision = precision * (tmp_ub ** 2)

            lb, ub = self.bounds(precision)
            return (1 / ub, 1 / lb)

        return Real(None, _invert)
