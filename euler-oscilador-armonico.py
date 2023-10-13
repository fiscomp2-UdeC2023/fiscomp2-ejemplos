#!/usr/bin/python3

# Copyright Roberto Navarro (2023)

# Archivo para resolver el oscilador armonico no lineal con el metodo de Euler

import numpy as np
import matplotlib.pyplot as plt

def f(x, t, w = 1.5):
    """Define el lado derecho de una ecuacion diferencial x'' = f(x,t)"""

    theta, v = x
    
    return np.array([v, -w**2 *np.sin(theta)])


#-------------------------------------
N = 5000   # pasos de tiempo
x = np.zeros([N,2])  # matriz de N filas, 2 columnas
dt = 0.01  # tamaño paso de tiempo
w = 1.5

# condiciones iniciales
x[0] = 0.1, -0.5  # similar a x[0,:]

# Metodo de Euler
for n in range(N-1):
    x[n+1] = x[n] + f(x[n], n*dt, w=w) * dt


theta = x[:,0]   # vector de N elementos 
v     = x[:, 1]  # N elementos

tiempo = np.arange(N) * dt

# # grafica posicion vs tiempo
# plt.plot(tiempo, theta, label="angulo")

# # grafica velocidad vs tiempo
# plt.plot(tiempo, v, label="velocidad")

# plt.xlabel("tiempo")
# plt.ylabel("angulo/velocidad")
# plt.legend()

# plt.show()


# grafica constante de movimiento
E = 0.5 * v**2 - w**2 * np.cos(theta)

plt.plot(tiempo, E)
plt.show()
