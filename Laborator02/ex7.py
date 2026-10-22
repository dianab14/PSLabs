import numpy as np
import matplotlib.pyplot as plt

fs = 1000
t = np.linspace(0, 0.1, int(0.1 * fs), endpoint = False)
f = 50
x = np.sin(2 * np.pi * f * t)

# a) pastram fiecare al 4-lea element, incepand cu primul
xa = x[::4]
ta = t[::4]

# b) pastram fiecare al 4-lea element, incepand cu al doilea
xb = x[1::4]
tb = t[1::4]

fig, axs = plt.subplots(3)
fig.suptitle('Grafic ex7')
axs[0].plot(t, x)
axs[0].set_ylabel('original')
axs[1].plot(ta, xa)
axs[1].stem(ta, xa)
axs[1].set_ylabel('x[0::4]')
axs[2].plot(tb, xb)
axs[2].stem(tb, xb)
axs[2].set_ylabel('x[1::4]')
axs[2].set_xlabel('t [s]')
plt.savefig('ex7.pdf')
plt.show()

#observatii
#a) sunt de 4 ori mai putine puncte deci semnalul nu se vede la fel de ondulat ca cel initial, dar se pastreaza nr de perioade
#b) al doilea semnal incepe putin mai tarziu decat primul, dar fiind mai putine puncte decat la primul arata tot ascutit