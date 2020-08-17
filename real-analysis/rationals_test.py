import pytest
from rationals import Q

@pytest.mark.parametrize(
    "n,m", [
        (Q(2, 1), Q(5,1)),
        (Q(1, 2), Q(1,5)),
        (Q(2, 2), Q(-3,17)),
        (Q(0, 2), Q(25,-17)),
    ])
def test_commutative(n, m):
    assert n + m == m + n
    assert n * m == m * n

@pytest.mark.parametrize(
    "n,m,k", [
        (Q(2, 1), Q(5,1), Q(17, 7)),
        (Q(1, 2), Q(1,5), Q(-2, 6)),
        (Q(2, 2), Q(-3,17), Q(5, 15)),
        (Q(0, 2), Q(25,-17), Q(-22,11)),
    ])
def test_assoc_dist(n, m, k):
    assert k + (n + m) == (k + m) + n
    assert k * (n + m) == (k * m) + (k * n)
