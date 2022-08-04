print("FIbonacci Test")
import fibonacci as fib

# Create the Fibonacci Object Device
print('Create the Fibonacci Object Device')
print('f=fib.Fibonacci(3,7)')
f=fib.Fibonacci(3,7)

# Show Seed values
print('Show Seed value f.a')
print(f.a)
print('Show Seed value f.b')
print(f.b)

# Set Seed Values
print('Set Seed Value f.b = 8')
f.b = 8
print(f.b)

print('Set Seed Value f.a = 4')
f.a = 4
print(f.a)

# Generate N values and report the last result
print('Generate N=10 values and report the last result')
print('f.generate(10)')
print(f.generate(10))


