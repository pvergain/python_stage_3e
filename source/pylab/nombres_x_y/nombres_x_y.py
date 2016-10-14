#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""Exemple d'utilisation du programme matplotlib.

Voir le module click pour l'utilisation en ligne de commandes.

(http://click.pocoo.org/dev/)

"""

from pylab import plot, show
from sympy import Symbol
from sympy import factor

def afficher_courbe_nombres():
    """Affichage d'une courbe
    
    Voir p.31 Python pour les maths
    """
    nombres_x=[1,2,3]
    nombres_y=[2,4,6]
    plot(nombres_x, nombres_y)
    show()

        

def exemple_factoriser():
    x=Symbol('x')
    y=Symbol('y')
    expr1=x**2-y**2
    facteur1 = factor(expr1)
    print(facteur1)


if __name__ == '__main__':
    exemple_factoriser()
    afficher_courbe_nombres()
