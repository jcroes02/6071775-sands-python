from gen_waves import *
from operation import *

def test_gen_sine_wave():
    """
    Test the sine wave generation function.
    
    Tests include:
    - Verifying correct output length for normal parameters
    - Checking initial value is zero
    - Verifying maximum amplitude matches expected value
    - Testing edge case with zero samples
    """
    t, y = gen_sine_wave(2,1,1, 1000) 
    assert len(t) == 1000
    assert y[0] == 0
    assert np.isclose(max(y), 2, atol=1e-6)

    t,y=gen_sine_wave(2,1,1,0)
    assert len(t) == 0 and len(y) == 0
    assert np.allclose(y,0)


def test_gen_square_signal():
    """
    Test the square wave generation function.
    
    Tests include:
    - Verifying correct output length for normal parameters
    - Checking initial value matches square wave characteristics
    - Verifying maximum amplitude matches expected value
    - Testing edge case with zero samples
    """
    t, y = gen_square_signal(2,1,1,1000)
    assert len(t) == 1000
    assert y[0] == 2
    assert np.isclose(max(y), 2, atol=1e-6)

    t, y = gen_square_signal(2,1,1,0)
    assert len(t) == 0 and len(y) == 0
    assert np.allclose(y,0)


def test_gen_sawtooth_signal():
    """
    Test the sawtooth wave generation function.
    
    Tests include:
    - Verifying correct output length for normal parameters
    - Checking initial value matches sawtooth wave characteristics
    - Verifying maximum amplitude matches expected value with tolerance
    - Testing edge case with zero samples
    """
    t, y = gen_sawtooth_signal(2,1,1,1000)
    assert len(t) == 1000
    assert y[0] == -2
    assert np.isclose(max(y), 2, atol=1e-2)

    t, y = gen_sawtooth_signal(2,1,1,0)
    assert len(t) == 0 and len(y) == 0
    assert np.allclose(y,0)


def test_gen_step():
    """
    Test the step function generation.
    
    Tests include:
    - Verifying correct output length for normal parameters
    - Checking step function behavior with negative step time
    - Verifying maximum amplitude matches expected value
    - Testing edge case with zero samples
    """
    t, y = gen_step(2,-1,1,1000)
    assert len(t) == 1000
    assert y[0] == 2
    assert np.isclose(max(y), 2, atol=1e-6)

    t, y = gen_step(2,1,1,0)
    assert len(t) == 0 and len(y) == 0
    assert np.allclose(y,0)

def test_time_shift():
    """
    Test the time_shift function with various test cases.
    
    Tests include:
    - Signal length verification
    - Shift timing and value verification
    - Negative shift handling
    - Zero shift case
    """
    t,v = gen_sine_wave(1, 1, 10, 2)
    v[500] = 1 

    shifted_signal = time_shift(v, 2, 100)
    assert len(shifted_signal) == 1000
    assert shifted_signal[700] == 1 

    shifted_signal = time_shift(v, -2, 100)
    assert len(shifted_signal) == 1000
    assert shifted_signal[300] == 1

    shifted_signal = time_shift(v, 0, 100)
    assert np.array_equal(shifted_signal, v)

def test_time_scale():
    """
    Test the time_scale function with various test cases.
    
    Tests include:
    - Signal length verification
    - Scaling factor validation
    - Edge case handling
    """
    t,v = gen_sine_wave(1,1,10,2)

    scaled_signal = time_scale(v, 2)
    assert len(scaled_signal) == 5000
    assert np.array_equal(scaled_signal, v[::2])

    scaled_signal = time_scale(v, 0.5)
    assert len(scaled_signal) == 20000

def test_amplitude_shift():
    """
    Test the amplitude_shift function with various test cases.
    
    Tests include:
    - Amplitude scaling verification
    - Negative scaling factor handling
    - Zero scaling case
    """
    t,v = gen_sine_wave(1,1,10,2)

    scaled_signal = amplitude_shift(v, 2)
    assert np.array_equal(scaled_signal, v * 2)

    scaled_signal = amplitude_shift(v, -1)
    assert np.array_equal(scaled_signal, v * -1)

    scaled_signal = amplitude_shift(v, 0)
    assert np.allclose(scaled_signal, 0)

def test_add_signals():
    """
    Test the add_signals function with various test cases.
    
    Tests include:
    - Element-wise addition verification
    - Different length handling (truncates to shorter)
    - Zero signal addition
    """
    t1, v1 = gen_sine_wave(1,1,10,2)
    t2, v2 = gen_sine_wave(3,2,10,2)

    added_signal = add_signals(v1, v2)
    assert len(added_signal) == min(len(v1), len(v2))

    signal3 = np.array([1, 2])
    added_signal = add_signals(v1, signal3)
    assert np.array_equal(added_signal, v1[:2] + signal3)

    zero_signal = np.zeros(3)
    added_signal = add_signals(v1, zero_signal)
    assert np.array_equal(added_signal, v1[:3])

def test_multiply_signals():
    """
    Test the multiply_signals function with various test cases.
    
    Tests include:
    - Element-wise multiplication verification
    - Different length handling (truncates to shorter)
    - Zero signal multiplication
    """
    t1, v1 = gen_sine_wave(1,1,10,2)
    t2, v2 = gen_sine_wave(3,2,10,2)
    
    multiplied_signal = multiply_signals(v1, v2)
    assert np.array_equal(multiplied_signal, v1 * v2)

    signal3 = np.array([1, 2])
    multiplied_signal = multiply_signals(v1, signal3)
    assert np.array_equal(multiplied_signal, v1[:2] * signal3)

    zero_signal = np.zeros(3)
    multiplied_signal = multiply_signals(v1, zero_signal)
    assert np.allclose(multiplied_signal, 0)