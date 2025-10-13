from gen_waves import *

def axis_shift(signal, shift_samples,M,fill_value=0):
    """
    Shift a signal along the time axis and apply a constant offset.
    
    Parameters:
    -----------
    signal : numpy.ndarray
        Input signal to be shifted
    shift_samples : int
        Number of samples to shift (positive = right shift, negative = left shift)
    M : float
        Constant value to add to the entire shifted signal
    fill_value : float, optional
        Value to fill the empty samples created by shifting (default is 0)
    
    Returns:
    --------
    numpy.ndarray
        Shifted signal with constant offset M applied
    """
    time_shift = np.roll(signal, shift_samples)
    if time_shift > 0:
        time_shift[:shift_samples] = fill_value
    elif time_shift < 0:
        time_shift[shift_samples:] = fill_value
    return M+time_shift

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