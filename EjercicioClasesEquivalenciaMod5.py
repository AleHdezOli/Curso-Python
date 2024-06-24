#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 10:43:52 2024

@author: alitahdezolivares
"""

ClaseEquiv0 = set()
ClaseEquiv1 = set()
ClaseEquiv2 = set()
ClaseEquiv3 = set()
ClaseEquiv4 = set()

for i in range(100):
  if i % 5 == 0:
      ClaseEquiv0.add(i)
      ClaseEquiv0.add(-i)
  elif i % 5 == 1:
      ClaseEquiv1.add(i)
      ClaseEquiv1.add(-i)
  elif i % 5 == 2:
      ClaseEquiv2.add(i)
      ClaseEquiv2.add(-i)
  elif i % 5 == 3:
      ClaseEquiv3.add(i)
      ClaseEquiv3.add(-i)
  else:
      ClaseEquiv4.add(i)
      ClaseEquiv4.add(-i)

print('Clase [0] =', sorted(ClaseEquiv0))
print('Clase [1] =', sorted(ClaseEquiv1))
print('Clase [2] =', sorted(ClaseEquiv2))
print('Clase [3] =', sorted(ClaseEquiv3))
print('Clase [4] =', sorted(ClaseEquiv4))

print('La intersección de los cinco conjuntos es:',
      sorted(ClaseEquiv0 & ClaseEquiv1 & ClaseEquiv2 & ClaseEquiv3 & ClaseEquiv4))

print('La unión de los cinco conjuntos es:',
      sorted(ClaseEquiv0 | ClaseEquiv1 | ClaseEquiv2 | ClaseEquiv3 | ClaseEquiv4))