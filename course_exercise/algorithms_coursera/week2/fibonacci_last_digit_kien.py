import sys

def fibonacci_last_digit(n):
    n = n % 60
    previous = 0
    current = 1
    if n<=1:
        return n
    else:
        for _ in range(n-1):
            previous, current = current, previous+current
            
        return current % 10

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(fibonacci_last_digit(n))