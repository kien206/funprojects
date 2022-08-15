# python3
import sys

def compute_min_refills(d, m, n, stops):
    num_refill = 0
    current_refill = 0
    if m >= d:
        num_refill == 0
    else:
        while current_refill <= n:
            last_refill = current_refill
            while (current_refill <= n) and (stops[current_refill+1]-stops[last_refill] <= m):
                current_refill += 1
            if current_refill == last_refill:
                return -1
            if current_refill <= n:
                num_refill += 1
    return num_refill
x = [200, 375, 550, 750]
print(x[1])
'''if __name__ == '__main__':
    n, l, _, *x = map(int, sys.stdin.read().split())
    print(compute_min_refills(x, n, l))
'''