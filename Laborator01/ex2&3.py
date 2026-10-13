import numpy as np
import matplotlib.pyplot as plt

#2
fs = 16000

#a)
f = 400
t = np.linspace(0, 1600 / fs, 1600, endpoint=False)

x = np.sin(2 * np.pi * f * t)

plt.plot(t, x)
plt.title('Grafic2a')

plt.savefig('ex2a.pdf')
plt.show()


#b)
f = 800
tt = np.linspace(0, 3, 3 * fs, endpoint=False)

y = np.sin(2 * np.pi * f * tt)

plt.plot(tt, y)
plt.title('Grafic2b')
plt.xlim([0, 0.01]) 

plt.savefig('ex2b.pdf')
plt.show()

#c)
f = 240
ttt = np.linspace(0, 0.03, 400)

z = f * ttt - np.floor(f * ttt)

plt.plot(ttt, z)

plt.title('Grafic2c')

plt.savefig('ex2c.pdf')
plt.show()

#d)
f = 300
tttt = np.linspace(0, 0.03, 400)

a = np.sign(np.sin(2 * np.pi * f * tttt))

plt.plot(tttt, a)

plt.title('Grafic2d')
plt.savefig('ex2d.pdf')
plt.show()

#e)
I = np.random.rand(128, 128)
plt.imshow(I)

plt.title('Grafic2e')
plt.savefig('ex2e.pdf')
plt.show()

#f)
I2 = np.zeros((128, 128))
I2[32:96, 32:96] = np.ones((64, 64)) * 0.5
I2[48:80, 48:80] = np.ones((32, 32))
plt.figure()
plt.imshow(I2, cmap='gray')
plt.title('Grafic2f')
plt.savefig('ex2f.pdf')
plt.show()

#3
#a) intervalul de timp este de 1 / 2000
#b) biti = fs * 3600 * 4; bytes = biti / 8
