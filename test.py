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

