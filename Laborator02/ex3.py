import numpy as np
import sounddevice as sd
import scipy.io.wavfile as wf

fs = 16000

# axa de timp: 2 secunde, 32000 de esantioane
t = np.linspace(0, 2, 2 * fs, endpoint = False)

# a) sinus 400 Hz
xa = np.sin(2 * np.pi * 400 * t)

# b) sinus 800 Hz
xb = np.sin(2 * np.pi * 800 * t)

# c) sawtooth 240 Hz
xc = 240 * t - np.floor(240 * t)

# d) square 300 Hz
xd = np.sign(np.sin(2 * np.pi * 300 * t))

sd.play(xa, fs)
sd.wait()

sd.play(xb, fs)
sd.wait()

sd.play(xc, fs)
sd.wait()

sd.play(xd, fs)
sd.wait()

#salvam al doilea semnal
wf.write('ex3.wav', fs, xb.astype(np.float32))

fs_citit, date = wf.read('semnal.wav')

print('fs citit:', fs_citit)
print('numar esantioane:', len(date))
print('identic cu originalul:', np.allclose(date, xb))