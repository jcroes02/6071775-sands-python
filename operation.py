from gen_waves import *

def time_shift(signal, shift, s_r):
    """
    Shift a signal in time by a specified amount.
    
    Parameters:
    -----------
    signal : numpy.ndarray
        Input signal array to be shifted
    shift : float
        Time shift amount in seconds (positive = delay, negative = advance)
    s_r : float
        Sample rate in samples per second
    
    Returns:
    --------
    numpy.ndarray
        Time-shifted signal array
    """
    shift_samples = int(shift * s_r)
    if shift_samples > 0:
        return np.concatenate((np.zeros(shift_samples), signal[:-shift_samples]))
    elif shift_samples < 0:
        return np.concatenate((signal[-shift_samples:], np.zeros(-shift_samples)))
    else:
        return signal

def amplitude_shift(signal,A):
    """
    Scale the amplitude of a signal by a constant factor.
    
    Parameters:
    -----------
    signal : numpy.ndarray
        Input signal to be scaled
    A : float
        Amplitude scaling factor
    
    Returns:
    --------
    numpy.ndarray
        Amplitude-scaled signal
    """
    return A*signal
    
def add_signals(signal1, signal2):
    """Add two signals together (must be same length)."""
    if len(signal1) != len(signal2):
        raise ValueError("Signals must have the same length")
    return signal1 + signal2

def multiply_signals(signal1, signal2):
    """Multiply two signals together."""
    if len(signal1) != len(signal2):
        raise ValueError("Signals must have the same length")
    return signal1 * signal2

def time_scale(t_signal,stretch):
    """
    Scale a time-domain signal by a stretch factor.
    
    Parameters:
    -----------
    t_signal : numpy.ndarray
        Time-domain input signal to be scaled
    stretch : float
        Stretch factor for time scaling
    
    Returns:
    --------
    numpy.ndarray
        Time-scaled signal
    """
    return t_signal*stretch