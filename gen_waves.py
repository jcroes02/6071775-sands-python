import numpy as np
import matplotlib.pyplot as plt

def generate_sine_wave(frequency, duration, sample_rate):
    t=np.linspace(0,duration, int(sample_rate))
    return np.sin(2*np.pi*frequency*t)

plt.plot(generate_sine_wave(0.5,2,100))

def generate_square_signal(A,F,duration,sample_rate):
    t=np.linspace(0,duration,int(sample_rate))
    return A*signal.square(np.pi*F*t)

plt.plot(generate_square_signal(10,1,10,100))

def gen_sawtooth_signal(A,F,duration,sample_rate):
    t=np.linspace(0,duration,int(sample_rate))
    return A*signal.sawtooth(2*np.pi*F*t)

plt.plot(gen_sawtooth_signal(10,1,10,100000))

def gen_step(S,E,L,SR):
    t=np.linspace(S,E,SR)
    v=np.where(t>L,1,0)
    return t,v

t,v=gen_step(-10,10,2,200)
plt.plot(t,v)