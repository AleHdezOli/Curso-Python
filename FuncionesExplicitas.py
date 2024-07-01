#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 15:17:43 2024

@author: alitahdezolivares
"""


#FUNCIONES EXPLÍCITAS


#Operaciones entre ellas

#Ejemplo 1

from sympy import symbols, sin
from sympy.plotting import plot
x = symbols('x')

fx = 0
for i in range (4):
    fx = fx + sin(i*x)
    

print(fx)
plot(fx)

#Ejemplo 2

from sympy import sin, symbols, Abs
from sympy.plotting import plot
def f(x):
    return Abs(Abs(x) - 1)
x = symbols('x')

plot(f(x))
plot(f(f(f(x))))
plot(f(x)*f(x), (x, -5, 5), line_color='red')

#Ejemplo 3

from sympy import sin, symbols, Abs, ln
from sympy.plotting import plot
def f(x):
    return (x + 3)*(x - 2)*(x + 4)

def g(x):
    return ln(x)

x = symbols('x')

plot(f(x))
plot(f(x), (x, -5, 3), line_color='blue')
plot(g(f(x)))

#Último ejemplo

from sympy import sin, symbols, Abs, ln
from sympy.plotting import plot
def f(x):
    return .1*(x + 3)*(x - 2)*(x + 4)

def g(x):
    return ln(x)

x = symbols('x')

g1 = plot(f(x), (x, -5, 5), line_color='blue', show=False)
g2 = plot(g(f(x)), (x, -5, 5), line_color='red', show=False)
g1.append(g2[0])
#g1.extend(g2)
g1.show()

#ACTIVIDAD 1

from sympy import symbols, ln, sqrt
from sympy.plotting import plot
def f(x):
    return sqrt(-1*x)

def g(x):
    return ln(x)

x = symbols('x')

plot(f(g(x)), (x, -5, 5), line_color='yellow')
plot(g(f(x)), (x, -5, 5), line_color='red')
plot(f(x)*g(x), (x, -5, 5), line_color='blue')

#Actividad 2

#No supe como hacerla Roberto, te iba a preguntar el viernes pero ya no llegué
#Esto fue lo que intenté. 

from sympy import symbols, sin, pi, diff
from sympy.plotting import plot

def f(x):
    for x in range(1, 100):
        return str(sin(2*pi*k**2*x)/4*pi**2*k**5 + x**2/2*k)

x = symbols('x')
k = symbols('k')

dx = diff(f(x), x)
print('La derivada es:', dx)

ddx = diff(dx, x)
print('La segunda derivada es:', ddx)

plot(f(x), (x, 1, 100), line_color='red')
plot(dx, (x, 1, 100), line_color='blue' )
plot(ddx, (x, 1, 100), line_color='yellow')


   










