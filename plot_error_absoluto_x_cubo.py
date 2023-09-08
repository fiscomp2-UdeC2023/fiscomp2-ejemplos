#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams
rcParams["font.size"] = 12

def f(x):
    return x**3


h = np.geomspace(1e-20, 0.1, 20)
df = ( f(1+h) - f(1) ) / h
error = np.abs( df - 3 )

plt.loglog(h, error, "o", label="error derivada adelantada")

hh = np.geomspace(h.min(), h.max(), 200)
plt.loglog(hh, 0.5*hh*6 + 2*2**(-52)/hh, label=r"error redondeo, $\varepsilon^\ast=2^{-52}$")
plt.loglog(hh, 0.5*hh*6 + 2*2**(-23)/hh, label=r"error redondeo, $\varepsilon^\ast=2^{-23}$")

plt.ylim(1e-11, 1e2)
plt.xlabel(r"$h$", fontsize=18)
plt.ylabel("error absoluto", fontsize=18)
plt.legend()
plt.tight_layout()
plt.show()
