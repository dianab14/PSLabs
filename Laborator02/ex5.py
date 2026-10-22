import numpy as np
import sounddevice as sd

fs = 16000
t = np.linspace(0, 1, fs, endpoint = False )

x = 100 * t - np.floor(100 * t)
y = 2560 * t - np.floor(2560 * t)

xy = np.concatenate((x,y))


sd.play(x, fs)
sd.wait()

sd.play(y, fs)
sd.wait()

sd.play(xy, fs)
sd.wait()

#observatie: cu cat frecventa e mai mare, cu atat sunetul e mai ascutit 