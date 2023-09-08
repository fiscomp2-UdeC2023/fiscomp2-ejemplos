#!/usr/bin/python3

# Copyright (c) 2023 - Roberto Navarro <roberto.navarro@udec.cl>

import numpy as np

def f(x):
    return x**3

# define limites
a, b = 1, 5

# define numero de puntos
N = 5
dx = (b-a) / (N-1)

print(f"Integral de x**3 entre a={a} y b={b}")
print(f"Integral exacta: {0.25*(b**4 - a**4)}")


suma = 0.0
for i in range(N-1):
    suma += f(a + i*dx) * dx
    
print(f"Integral numerica con for: {suma}")

suma = np.sum( f(np.linspace(a, b, N-1, endpoint=False)) * dx )
print(f"Integral numerica con linspace: {suma}")

suma = np.sum( f(np.arange(a, b, dx)) * dx )
print(f"Integral numerica con arange: {suma}")
