"""Copyright (c) 2023 Roberto Navarro <roberto.navarro@udec.cl>
 
   Este script muestra cómo derivar datos que presenten ruido aleatorio.

   En este caso, crearemos datos ruidosos a partir de una función
   contínua y perturbaremos la curva con datos aleatorios.
"""

import numpy as np
import matplotlib.pyplot as plt

def deriv(x, y, n=1):
    """Deriva una secuencia de datos {x[i], y[i]} usando diferencias centradas, de la forma:

        dy[i] = ( y[i+2n] - y[i-2n] ) / (x[i+2n] - x[i-2n] )

       donde `n` es equivalente a `h` en métodos usuales de derivadas centradas. """
    
    step=2*n
    return (y[step:] - y[:-step])/(x[step:] - x[:-step])


# creamos una sequencia de valores {x[i], y[i]} a partir de funciones continuas
x = np.linspace(0,2*np.pi,512)
y = np.sin(x) * np.sin(11*x) 

# creamos otra secuencia y_noisy[i] que es una perturbacion aleatoria de y[i]
eps = 1
y_noisy = y * ( 1 + eps * (2*np.random.random(len(x))-1))


fig, ax = plt.subplots(nrows=3,ncols=1, sharex=True)

# Muestra derivada de y_noisy usando derivadas finitas con n=1
ax[0].plot(x, y_noisy, label=r"Noisy $y_i$")
ax[1].plot(x[1:-1], deriv(x,y_noisy), label=r"Noisy deriv $y_i$")

# Derivada de y_noisy pero con n>1. 
N=10
ax[2].plot(x[N:-N], deriv(x,y_noisy,n=N), label=r"Noisy deriv $y_i$")

# Muestra la derivada de la serie y[i] para compararla con las derivadas de datos ruidosos
ax[0].plot(x, y, lw=3, label=r"$y_i$")
ax[1].plot(x[1:-1], deriv(x,y), lw=3, label=r"Deriv $y_i$")
ax[2].plot(x[1:-1], deriv(x,y), lw=3, label=r"Deriv $y_i$")

# La conclusion es que la derivada de datos ruidosos se acerca mas al
# de la funcion continua si aumentamos `n` en vez de disminuir `n`.


for a in ax:
    a.legend()
    a.set_xlabel(r"$x_i$ data")
    a.set_ylabel(r"deriv $y_i$ data")

plt.tight_layout()
plt.show()
