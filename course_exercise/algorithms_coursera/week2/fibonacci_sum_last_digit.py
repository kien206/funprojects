import sys

def fibonacci_sum_last_digit(n):
    n = n% 60
    previous = 0
    current = 1
    
    for i in range(n+1):
        previous, current = current, previous+current
        
        sum_last_digit = (current -1) % 10
    if n <= 1:
        return n
    else:
        return sum_last_digit

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(fibonacci_sum_last_digit(n))