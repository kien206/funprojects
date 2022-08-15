'''def fibonacci_slow(n):
    if n <= 1:
        return n
    else:
        return fibonacci_slow(n-1) + fibonacci_slow(n-2)'''
# takes 56000 years at 1Ghz to calc fibonacci(100)
def fibonacci_fast(n):
    previous = 0
    current = 1
    if n <= 1:
        return n
    for _ in range(n-1):
        previous, current = current, previous + current
    return current
n = int(input())
print(fibonacci_fast(n))