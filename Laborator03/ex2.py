import numpy as np
import matplotlib.pyplot as plt
import math
from matplotlib.animation import FuncAnimation

ANIMATIE = True

f = 3
N = 1000 #nr de esantioane
t = np.linspace(0, 1, N, endpoint=False)
x = np.sin(2 * np.pi * f * t) #semnal sinusoidal 

y = x * math.e ** (-2j * math.pi * t)
idx = 620     #esantionul marcat

def plan_complex(ax, z, titlu):
    # culoarea fiecarui punct depinde de distanta fata de origine
    sc = ax.scatter(z.real, z.imag, c=np.abs(z), cmap='viridis', s=4)
    ax.set_title(titlu)
    ax.set_xlabel('Real')
    ax.set_ylabel('Imag')
    ax.axis('equal')
    return sc
 
 
# Figura 1 (varianta statica)
fig, axs = plt.subplots(1, 2, figsize=(10, 4))

axs[0].plot(t, x)
axs[0].axhline(0, color='black', linewidth=0.8)
axs[0].plot([t[idx], t[idx]], [0, x[idx]], 'r')
axs[0].plot(t[idx], x[idx], 'ro')
axs[0].set_title('x[n] in timp')
axs[0].set_xlabel('Timp [s]')
axs[0].set_ylabel('Amplitudine')

sc = axs[1].scatter(y.real, y.imag, c=np.abs(y), cmap='viridis', s=4)
axs[1].plot([0, y[idx].real], [0, y[idx].imag], 'r-o')
axs[1].set_title('y[n] = x[n] * e^(-2*pi*j*n)')
axs[1].set_xlabel('Real')
axs[1].set_ylabel('Imag')
axs[1].axis('equal')

plt.savefig('ex2_fig1.pdf')
plt.show()

# Figura 2 (varianta statica)
omegas = [1, 2, f, 7]
zs = []
for w in omegas:
    zs.append(x * math.e ** (-2j * math.pi * w * t)) #pune in vector infasurarile in functie de omega

fig, axs = plt.subplots(2, 2, figsize=(8, 8))
for ax, z, w in zip(axs.flat, zs, omegas):
    ax.scatter(z.real, z.imag, c=np.abs(z), cmap='viridis', s=4)
    ax.axhline(0, color='black', linewidth=0.8)
    ax.axvline(0, color='black', linewidth=0.8)
    ax.set_title('omega = ' + str(w))
    ax.set_xlabel('Real')
    ax.set_ylabel('Imag')
    ax.axis('equal')
plt.savefig('ex2_fig2.pdf')
plt.show()
 
# Variantele animate
def animeaza(fig, axs, zs, pas=7):
    scs = []
    pcts = []
    for ax, z in zip(axs, zs):
        m = np.max(np.abs(z)) * 1.1
        sc = ax.scatter([], [], s=4, cmap='viridis', vmin=0, vmax=np.max(np.abs(z)))
        pct, = ax.plot([], [], 'ro')
        ax.set_xlim(-m, m)
        ax.set_ylim(-m, m)
        ax.set_aspect('equal')
        scs.append(sc)
        pcts.append(pct)
 
    def update(k):
        for sc, pct, z in zip(scs, pcts, zs):
            sc.set_offsets(np.c_[z.real[:k], z.imag[:k]])
            sc.set_array(np.abs(z[:k]))
            pct.set_data([z[k - 1].real], [z[k - 1].imag])
        return scs + pcts
 
    return FuncAnimation(fig, update, frames=range(1, len(zs[0]) + 1, pas), interval=20)
 
 
if ANIMATIE:
    fig_a1, ax_a1 = plt.subplots()
    ax_a1.set_title('Fig. 1 animata: y[n] pe cercul unitate')
    anim1 = animeaza(fig_a1, [ax_a1], [y])
 
    fig_a2, ax_a2 = plt.subplots(2, 2, figsize=(8, 8))
    for ax, w in zip(ax_a2.flat, omegas):
        ax.set_title('omega = ' + str(w))
    anim2 = animeaza(fig_a2, list(ax_a2.flat), zs)
    plt.show()
 