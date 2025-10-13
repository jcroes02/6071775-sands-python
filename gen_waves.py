import numpy as np
from scipy import signal

def gen_sine_wave(A,F,duration, sample_rate):
    """
    Generate a sine wave signal.
    
    Parameters:
    -----------
    A : float
        Amplitude of the sine wave
    F : float
        Frequency of the sine wave in Hz
    duration : float
        Duration of the signal in seconds
    sample_rate : int
        Sampling rate in samples per second
    
    Returns:
    --------
    t : numpy.ndarray
        Time array from 0 to duration
    v : numpy.ndarray
        Sine wave signal values
    """
    t=np.linspace(0,duration,sample_rate)
    v=A*np.sin(2*np.pi*F*t)
    return t,v

def gen_square_signal(A,F,duration,sample_rate):
    """
    Generate a square wave signal.
    
    Parameters:
    -----------
    A : float
        Amplitude of the square wave
    F : float
        Frequency of the square wave in Hz
    duration : float
        Duration of the signal in seconds
    sample_rate : int
        Sampling rate in samples per second
    
    Returns:
    --------
    t : numpy.ndarray
        Time array from 0 to duration
    v : numpy.ndarray
        Square wave signal values
    """
    t=np.linspace(0,duration,sample_rate)
    v=A*signal.square(np.pi*F*t)
    return t,v

def gen_sawtooth_signal(A,F,duration,sample_rate):
    """
    Generate a sawtooth wave signal.
    
    Parameters:
    -----------
    A : float
        Amplitude of the sawtooth wave
    F : float
        Frequency of the sawtooth wave in Hz
    duration : float
        Duration of the signal in seconds
    sample_rate : int
        Sampling rate in samples per second
    
    Returns:
    --------
    t : numpy.ndarray
        Time array from 0 to duration
    v : numpy.ndarray
        Sawtooth wave signal values
    """
    t=np.linspace(0,duration,sample_rate)
    v=A*signal.sawtooth(2*np.pi*F*t)
    return t,v

def gen_step(A,L,duration,sample_rate):
    """
    Generate a step function signal.
    
    Parameters:
    -----------
    A : float
        Amplitude of the step function
    L : float
        Time location where the step occurs (in seconds)
    duration : float
        Duration of the signal in seconds
    sample_rate : int
        Sampling rate in samples per second
    
    Returns:
    --------
    t : numpy.ndarray
        Time array from 0 to duration
    v : numpy.ndarray
        Step function signal values (0 before L, A after L)
    """
    t=np.linspace(0,duration,sample_rate)
    v=A*np.where(t>L,1,0)
    return t,v
