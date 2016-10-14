#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""Exemples de code Python basés sur matplotlib .

- matplotlib (http://matplotlib.org/index.html)

"""

from pylab import plot, show
from sympy import Symbol

def afficher_courbe_nombres():
    """Affichage d'une courbe en employant le module Python matplotlib
    
    Voir p.31 Python pour les maths
    """
    nombres_x=[1,2,3]
    nombres_y=[2,4,6]
    plot(nombres_x, nombres_y)
    show()

    
if __name__ == '__main__':
    afficher_courbe_nombres()
