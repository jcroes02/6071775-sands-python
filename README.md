Packages required to run the files
-Python 3.x
-NumPy
-Scipy

fucntions within wave generator file
-gen_sine_wave(): generates a sine wave with adjustable frequencies, amplitudes and duration
-gen_square_signal(): generates a square wave with adjustable frequencies, amplitudes and duration
-gen_sawtooth_signal():generates a sawtooth wave with adjustable frequencies, amplitudes and duration
-gen_step(): generates a heaviside step function with adjustable begin and endpoints and amplitudes

functions in operator file
-axis_shift():shifts signal in time and vertical axis
-amplitude_shift(): scale signal amplitude
-add_signals(): add two signals together
-multiply_signal(): multiply two signals
-time_scale(): scale time axis to compress/stetch signal

functions in test file
-tests the wave generator file