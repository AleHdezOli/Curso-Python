#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 10:12:03 2024

@author: alitahdezolivares
"""

from math import sqrt

print('Hola, vamos a resolver una ecuación de segundo grado:')
print('ax^2 + bx + c = 0')

a, b, c = [float(input(f'Dame el coeficiente {coef}:')) for coef in ('a', 'b', 'c')]

discriminante = (b**2)-(4*a*c)

if discriminante < 0: 
    print(f'La ecuación no tienen soluciones reales.')
else: 
    raiz = sqrt(discriminante)
    x1 = (-b + raiz)/(2*a)
    if discriminante !=0:
        x2 = (-b - raiz) / (2*a)
        print(f'Las soluciones son {x1} y {x2}.')
    else:
        print(f'La única solución es x = {x1}')
        
        



