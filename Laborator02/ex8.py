import numpy as np
import matplotlib.pyplot as plt

alpha = np.linspace(-np.pi / 2, np.pi / 2, 100)
sin = np.sin(alpha)
taylor = alpha
pade = (alpha - 7 * alpha ** 3 / 60) / (1 + alpha ** 2 / 20)

fig, axs = plt.subplots(2)
fig.suptitle('Grafic ex8')
axs[0].plot(alpha, sin, label='sin(a)')
axs[0].plot(alpha, taylor, '--', label='a (Taylor)')
axs[0].plot(alpha, pade, ':', label='Pade')
axs[0].legend()
axs[1].plot(alpha, sin - taylor, label='eroare Taylor')
axs[1].plot(alpha, sin - pade, label='eroare Pade')
axs[1].legend()
plt.savefig('ex8.pdf')
plt.show()
 
# eroarea pe axa Oy logaritmica
plt.figure()
plt.semilogy(alpha, np.abs(sin - taylor) + 1e-18, label='|eroare| Taylor')
plt.semilogy(alpha, np.abs(sin - pade) + 1e-18, label='|eroare| Pade')
plt.legend()
plt.title('Eroare cu axa Oy logaritmica')
plt.savefig('ex8_log.pdf')
plt.show()
