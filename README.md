# FIBONACCI

    This uses a private circuitpython build located at:

    https://github.com/latkinso42/circuitpython branch fib

    Usage:

        import fibonacci as fib

        f = fib.Fibonacci(a,b) creates a fibonacci generator object with

        initial seeds a and b. The generate algorithm does not use recursion
	but iteration and is fast. Normal operation is the sum of the last two
	results of the Fibonacci sequence, thus the need for two seeds.

        The library allows one to get, set or clear the seeds.

        Please see the example test code.py.

	Some obvious limit constraints are provided.