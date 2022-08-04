# The Fibonacci Adventure in Extending CircuitPython

Before actually contributing to CircuitPython, I thought I might try a toy extension.
What could I do that would be simple? A Fibonacci Generator! You know the sequence
0,1,1,2,3,5,8,13,... where any number in the sequence is the sum of the proceding two numbers.

However, I would generalize this so that the user could define a virtual device by
supplying the first two 'seed' numbers. Then provide a function say generate(N) to iterate over
sequence N times and return the result. The math was trivial, but the methodolgy for CircuitPython
extension would be learned!

This example is simple enough that one can follow the extension as a template without
having to stretch into the hardware specifics the first time.

I followed the links and pages devoted to contributing, however that was only the beginning of the adventure.
I found some of the material dated and got lots of help on Discord. Basically it went like this:

1) Install (or update) VirtualBox;
2) Put a new 64bit Ubuntu ISO on the Vbox.
3) Create a build dir for circuitpython and follow direction to create the build environment.
4) Create GitHub (I updated my old one).

I initially used the example under "Simple 42", but quickly began to copy the design patterns from pulseio and busio.
Since my target was the Raspberry Pi Pico, I put my new code in circuitpython/ports/raspberrypi/common-hal/fibonacci.
I also made changes in circiutpython/shared-bindings/fibonacci.
There were a few lines added to a few files in circuitpython/py/circuitpy_*

The macros in py/runtime.c and py/argcheck.c helped such that the resulting virtual device has readable and settable parameters, as well as some marcos helpers for limit checking which automatically raise errors (very easy to use!).

Finally one can create the device as so:

   >>>import fibonacci as fib

   >>>f = fib.Fibonacci(3,7)

   >>>f.generate(10)

   >>>487

One can also get or set the seeds.

   >>>f.a = 11

   >>>f.a

   >>>11

Very basic, elementary module to get you started. I learned an incredible amount!
Now I'm ready to tackle a more difficult extension with some special hardware functionality.

Please feel free to clone and test the fib branch referenced at https://github.com/latkinso42/circiuitpython.
Test CPy code is at https://github.com/latkinso42/fibonacci

Enjoy!