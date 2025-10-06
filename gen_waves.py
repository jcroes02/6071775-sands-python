import numpy as np
from scipy import signal

def gen_sine_wave(A,F,duration, sample_rate):
    t=np.linspace(0,duration,sample_rate)
    v=A*np.sin(2*np.pi*F*t)
    return t,v

def gen_square_signal(A,F,duration,sample_rate):
    t=np.linspace(0,duration,sample_rate)
    v=A*signal.square(np.pi*F*t)
    return t,v

def gen_sawtooth_signal(A,F,duration,sample_rate):
    t=np.linspace(0,duration,sample_rate)
    v=A*signal.sawtooth(2*np.pi*F*t)
    return t,v

def gen_step(A,L,duration,sample_rate):
    t=np.linspace(0,duration,sample_rate)
    v=A*np.where(t>L,1,0)
    return t,v
