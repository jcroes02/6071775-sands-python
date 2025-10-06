from gen_waves import *
from operation import *

t, y = gen_sine_wave(2,1,1, 1000) #amplitude of 2, frequency of 1, duration of 1 second with 1000 sample_rates
assert len(t) == 1000
assert y[0] == 0
assert np.isclose(max(y), 2, atol=1e-6)

t, y = gen_square_signal(2,1,1,1000)#amplitude of 2, frequency of 1, duration of 1 second with 1000 sample_rates
assert len(t) == 1000
assert y[0] == 2
assert np.isclose(max(y), 2, atol=1e-6)

t, y = gen_sawtooth_signal(2,1,1,1000)#amplitude of 2, frequency of 1, duration of 1 second with 1000 sample_rates
assert len(t) == 1000
assert y[0] == -2
assert np.isclose(max(y), 2, atol=1e-2)

t, y = gen_step(2,-1,1,1000)#amplitude of 2, step begins at -1, 1000 sample rates
assert len(t) == 1000
assert y[0] == 2
assert np.isclose(max(y), 2, atol=1e-6)