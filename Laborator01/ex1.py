import numpy as np
import matplotlib.pyplot as plt

#ex1
#a)
t = np.linspace(0, 0.03, 100)

#b)
x = np.cos(520 * np.pi * t + np.pi / 3)
y = np.cos(280 * np.pi * t - np.pi / 3)
z = np.cos(120 * np.pi * t + np.pi / 3)

fig, axs = plt.subplots(3)
fig.suptitle('Grafic1b')
axs[0].plot(t, x)
axs[1].plot(t, y)
axs[2].plot(t, z)
for ax in axs.flat:
    ax.set_xlim([0, 0.03])
    
plt.savefig('ex1b.pdf')   
plt.show()

#c)
fs = 200

N = int(np.round(0.03 * fs)) + 1     
n = np.linspace(0, 0.03, N)       
xn = np.cos(520 * np.pi * n + np.pi / 3)
yn = np.cos(280 * np.pi * n - np.pi / 3)
zn = np.cos(120 * np.pi * n + np.pi / 3)
 
fig, axs = plt.subplots(3)
fig.suptitle('Grafic1c')

axs[0].plot(t, x)
axs[0].stem(n, xn)
axs[1].plot(t, y)
axs[1].stem(n, yn)
axs[2].plot(t, z)
axs[2].stem(n, zn)
for ax in axs.flat:
    ax.set_xlim([0, 0.03])
plt.savefig('ex1c.pdf')
plt.show()
