#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 10:41:57 2024

@author: alitahdezolivares
"""

from sympy import symbols, Integral, sin


x = symbols('x')
intsen = Integral(sin(x), (x,-1,1))
print('El resultado es:', intsen.evalf())


from sympy import symbols, integrate, exp, oo

x = symbols('x')
print(integrate(exp(-x), (x, 0, oo)))

