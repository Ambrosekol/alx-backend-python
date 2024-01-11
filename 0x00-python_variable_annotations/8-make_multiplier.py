#!/usr/bin/env python3

"""
Write a type-annotated function make_multiplier that takes
a float multiplier as argument and returns a function
that multiplies a float by multiplier.
"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Write a type-annotated function make_multiplier that takes
    a float multiplier as argument and returns a function
    that multiplies a float by multiplier.
    """

    def multiply(val: float) -> float:
        """
        This function will be returned my who calls it
        """
        return val * multiplier

    return multiply
