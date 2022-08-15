import sys

def pisanoPeriod(m):
    previous = 0
    current = 1
    
    for i in range(m*m):
        previous, current = current, (previous+current)%m
        if previous == 0 and current == 1:
            return i +1

def fibonacci_huge(n, m):
    pisano_Period = pisanoPeriod(m)

    n = n % pisano_Period

    previous = 0
    current  = 1
    if n == 0:
        return n
    else:
        for _ in range(n - 1):
            previous, current = current, previous + current

        return current % m

if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(fibonacci_huge(n, m))