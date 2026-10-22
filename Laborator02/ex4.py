import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 0.1, 1600, endpoint = False)

xa = np.sin(2 * np.pi * 400 * t)

xc = 240 * t - np.floor(240 * t)

suma = xa + xc

fig, axs = plt.subplots(3)
fig.suptitle('Grafic ex4')
axs[0].plot(t, xa)
axs[0].set_ylabel('sinusoidala')
axs[1].plot(t, xc)
axs[1].set_ylabel('sawtooth')
axs[2].plot(t, suma)
axs[2].set_ylabel('suma')
plt.savefig('ex4.pdf')
plt.show()
