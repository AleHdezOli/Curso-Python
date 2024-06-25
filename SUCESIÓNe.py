#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 10:53:41 2024

@author: alitahdezolivares
"""

import math

x = 2

for i in range (100000):
    x = (1 + 1/x)**x

print('El número e es:', x)

import numpy as np

e = []
for n in range (1, 100000):
    aprox = (1 + 1/n)**n
    e.append(aprox)
    print(f'{n:>7}{aprox:>18.15f}')
    
print('El valor de e con numpy es:', np.e)