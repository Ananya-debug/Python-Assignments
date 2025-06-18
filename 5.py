import math


def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


fib_cache = {}

def fibonacci_memo(n):
    if n in fib_cache:
        return fib_cache[n]
    if n == 0:
        fib_cache[n] = 0
    elif n == 1:
        fib_cache[n] = 1
    else:
        fib_cache[n] = fibonacci_memo(n-1) + fibonacci_memo(n-2)
    return fib_cache[n]


def is_perfect_square(x):
    s = int(math.sqrt(x))
    return s * s == x

def is_fibonacci(num):
    return is_perfect_square(5 * num * num + 4) or is_perfect_square(5 * num * num - 4)


print("First 7 Fibonacci numbers using 'yield' and 'next()':")
fib_gen = fibonacci_generator()
for _ in range(7):
    print(next(fib_gen), end=' ')

print("\n\nFirst 7 Fibonacci numbers using Memoization (Dictionary):")
for i in range(7):
    print(fibonacci_memo(i), end=' ')


user_num = int(input("\n\nEnter a number to check if it is a Fibonacci number: "))
if is_fibonacci(user_num):
    print(user_num, "is a Fibonacci number.")
else:
    print(user_num, "is NOT a Fibonacci number.")
