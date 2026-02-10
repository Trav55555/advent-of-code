"""Math utilities that come up repeatedly in Advent of Code."""

from functools import reduce
from math import gcd, lcm


def lcm_many(*args: int) -> int:
    """LCM of arbitrarily many integers.

    >>> lcm_many(4, 6, 10)
    60
    """
    return reduce(lcm, args)


def gcd_many(*args: int) -> int:
    """GCD of arbitrarily many integers."""
    return reduce(gcd, args)
