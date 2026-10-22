import numpy as np
import matplotlib.pyplot as plt

A = 2 # amplitudinea
f = 20 #frecventa
t = np.linspace(0, 1, 2000, endpoint = False)

s1 = np.sin(2 * np.pi * f * t + 0)
s2 = np.sin(2 * np.pi * f * t + np.pi / 2)
s3 = np.sin(2 * np.pi * f * t + np.pi / 3)
s4 = np.sin(2 * np.pi * f * t + np.pi)

fig, axs = plt.subplots(4)
fig.suptitle('Grafic ex2')
axs[0].plot(t, s1)
axs[1].plot(t, s2)
axs[2].plot(t, s3)
axs[3].plot(t, s4)
plt.savefig('ex2.pdf')
plt.show()

z = np.random.normal(0, 1, len(t))
gamma1 = np.linalg.norm(s1) / (np.linalg.norm(z) * np.sqrt(0.1))
gamma2 = np.linalg.norm(s1) / (np.linalg.norm(z) * np.sqrt(1))
gamma3 = np.linalg.norm(s1) / (np.linalg.norm(z) * np.sqrt(10))
gamma4 = np.linalg.norm(s1) / (np.linalg.norm(z) * np.sqrt(100))

fig, axs = plt.subplots(4)
fig.suptitle('Grafic ex2 semnal + zgomot')
axs[0].plot(t, s1 + gamma1 * z)
axs[0].set_ylabel('SNR=0.1')
axs[1].plot(t, s1 + gamma2 * z)
axs[1].set_ylabel('SNR=1')
axs[2].plot(t, s1 + gamma3 * z)
axs[2].set_ylabel('SNR=10')
axs[3].plot(t, s1 + gamma4 * z)
axs[3].set_ylabel('SNR=100')
axs[3].set_xlabel('t [s]')
plt.savefig('ex2zgomot.pdf')
plt.show()