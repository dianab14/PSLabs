import numpy as np
import matplotlib.pyplot as plt
import math

fs = 200
t = np.linspace(0, 1, fs, endpoint=False)
f1, f2, f3 = 8, 36, 91
x = np.sin(2 * np.pi * f1 * t) + 2 * np.cos(2 * np.pi * f2 * t) + 0.2 * np.sin(2 * np.pi * f3 * t)

def dft_bucle(x):
    N = len(x)
    X = np.zeros(N, dtype=complex)
    for w in range(N): #parcurgere frecvente testate
        for n in range(N): #parcurgere esantioane
            X[w] = X[w] + x[n] * math.e ** (-2j * math.pi * n * w / N)
    return X
 
 
def dft_matrice(x):
    N = len(x)
    F = np.zeros((N, N), dtype=complex)
    for k in range(N):
        for n in range(N):
            F[k, n] = math.e ** (-2j * math.pi * k * n / N)
    return F @ x
 
X1 = dft_bucle(x)
X2 = dft_matrice(x)
print(np.allclose(X1, X2)) #verficare daca sunt identice
 
omega = np.arange(0, 100)
modul = np.abs(X1[:100])
 
fig, axs = plt.subplots(1, 2, figsize=(10, 4))
axs[0].plot(t, x)
axs[0].set_title('Semnalul x(t)')
axs[0].set_xlabel('Timp [s]')
axs[0].set_ylabel('Amplitudine')
axs[1].stem(omega, modul)
axs[1].set_title('Modulul transformatei Fourier')
axs[1].set_xlabel('Frecventa de infasurare omega [Hz]')
axs[1].set_ylabel('|X(omega)|')
plt.savefig('ex3.pdf')
plt.show()

