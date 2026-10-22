import numpy as np
import matplotlib.pyplot as plt

A = 2 # amplitudinea
f = 20 #frecventa
faza = np.pi / 3
t = np.linspace(0, 1, 2000, endpoint = False)

sinus = A * np.sin(2 * np.pi * f * t + faza)
cosinus = A * np.cos(2 * np.pi * f * t + faza - np.pi/2) 

fig, axs = plt.subplots(2)
fig.suptitle('Grafic ex1')
axs[0].plot(t, sinus)
axs[0].set_ylabel('sinus')
axs[1].plot(t, cosinus)
axs[1].set_ylabel('cosinus')
plt.savefig('ex1.pdf')
plt.show()
