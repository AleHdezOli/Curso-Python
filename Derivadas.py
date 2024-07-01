#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 14:33:06 2024

@author: alitahdezolivares
"""

#Derivadas

#Ejemplo 1

from sympy import symbols, diff, sin, exp
x  = symbols('x')
dx = diff(sin(x)/x, x)
print("La derivada es: ", dx)
dxEval = dx.subs(x, 4).evalf()
print("La derivada evaluada en x = 4 es: ", dxEval)

#Actividad 1

from sympy import symbols, diff, sin, exp, ln

x  = symbols('x')
fx = ln(4**(7*x**2)/(5*exp(3*x**5)))
dx = diff(fx, x)
print("La derivada es: \n {0}  \n= {1} ".format(dx, dx.simplify()))
#Evaluando en el puntos críticos
#print(
puntoEvaluacion = 0
dxEval = dx.subs(x, puntoEvaluacion).evalf()
print("La derivada evaluada en x = {0} es: {1}".format(puntoEvaluacion, dxEval))
puntoEvaluacion = 1.08967
dxEval = dx.subs(x, puntoEvaluacion).evalf()
print("La derivada evaluada en x = {0} es: {1}".format(puntoEvaluacion, dxEval))

#Actividad 2

from sympy import symbols, diff, sin, exp, ln, tan, sqrt

x  = symbols('x')
fx = tan(exp(2*sin(x))/4*x)**sqrt(x)
dx = diff(fx, x)
print('La derivada es:', dx)
