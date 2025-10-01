from gen_waves import *

def time_shift(
    

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
    