from gen_waves import *

def axis_shift(signal, shift_samples,M,fill_value=0):
    time_shift = np.roll(signal, shift_samples)
    if time_shift > 0:
        time_shift[:shift_samples] = fill_value
    elif time_shift < 0:
        time_shift[shift_samples:] = fill_value
    return M+time_shift

def amplitude_shift(signal,A):
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
    return t_signal*stretch

