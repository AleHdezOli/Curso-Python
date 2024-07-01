#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 12:49:49 2024

@author: alitahdezolivares
"""

#INTEGRALES

#Usando la función INTEGRAL

from sympy import symbols, Integral, sin

x = symbols('x')
intsen = Integral(sin(x), (x,-1,1))
print('El resultado es:', intsen.evalf())

#Usando la función INTEGRATE

from sympy import symbols, integrate, exp, oo

x = symbols('x')
print(integrate(exp(-x), (x, 0, oo)))

#Actividad con función INTEGRAL

from sympy import symbols, Integral, sqrt

x = symbols('x')
intsqrt = Integral(sqrt(1 + x**3), (x,-1,1))
print('El resultado es:', intsqrt.evalf())

#Actividad con función INTEGRATE

from sympy import symbols, integrate, sqrt

x = symbols('x')
print(integrate(sqrt(1 + x**3), (x, -1, 1)))
