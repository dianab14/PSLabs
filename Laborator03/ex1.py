import numpy as np
import matplotlib.pyplot as plt
import math

N = 8 #nr de esantioane
F = np.zeros((N, N), dtype=complex)
for k in range(N):
    for n in range(N):
        F[k, n] = math.e ** (-2j * math.pi * k * n / N) # matricea fourier
 
# fiecare linie a matricei in cate un subplot: partea reala si partea imaginara
n = np.arange(N)
fig, axs = plt.subplots(N, 2, figsize=(10, 12), sharex=True, sharey=True)
fig.suptitle('Grafic ex1', fontsize=14)
for k in range(N):
    axs[k, 0].stem(n, F[k].real)
    axs[k, 1].stem(n, F[k].imag)
    axs[k, 0].set_ylabel('k = ' + str(k))
    axs[k, 0].set_ylim(-1.3, 1.3)
axs[0, 0].set_title('Partea reala')
axs[0, 1].set_title('Partea imaginara')
plt.tight_layout()
plt.savefig('ex1.pdf')
plt.show()


# verificare unitaritate: F^H F trebuie sa fie N * I
FhF = F.conj().T @ F
print('F^H F == N * I ?', np.allclose(FhF, N * np.eye(N)))
print('norma diferentei:', np.linalg.norm(FhF - N * np.eye(N)))