#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""Exemples de code Python basés sur sympy.

- sympy (http://docs.sympy.org/latest/index.html)

"""

from sympy import Symbol
from sympy import factor


def exemple_factoriser():
    """Factorisation d'une expression en employant le module Python sympy"""
    x=Symbol('x')
    y=Symbol('y')
    expr1=x**2-y**2
    facteur1 = factor(expr1)
    print(facteur1)


if __name__ == '__main__':
    exemple_factoriser()
