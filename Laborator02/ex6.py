import numpy as np
import matplotlib.pyplot as plt

fs = 1600
t = np.linspace(0, 0.1, int(0.1 * fs), endpoint = False)

a = np.sin(2 * np.pi * (fs / 2) * t) # nu se recunoaste sinusul
b = np.sin(2 * np.pi * (fs / 4) * t) # se vede un sinus, dar cu colturi pentru ca are putine puncte
c = np.sin(2 * np.pi * 0 * t) #semnalul este reprezentat de o linie dreapta la nivelul lui 0

fig, axs = plt.subplots(3)
fig.suptitle('Grafic ex6')
axs[0].plot(t, a)
#axs[0].set_ylim([-1, 1])
axs[0].set_ylabel('a')
axs[1].plot(t, b)
axs[1].set_ylabel('b')
axs[2].plot(t, c)
axs[2].set_ylabel('c')
plt.savefig('ex6.pdf')
plt.show()