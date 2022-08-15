# Uses python3
import sys

def get_optimal_value(capacity, weight, value):
    
    index = list(range(len(value)))

    for v, w in zip(value, weight):
        ratio = v/w
        index.sort(key=lambda i: ratio[i], reverse=True)

    max_value = 0
    fractions = [0]*len(value)
    
    for i in index:
        if weight[i] <= capacity:
            fractions[i] = 1
            max_value += value[i]
            capacity -= weight[i]
        else:
            fractions[i] = capacity/weight[i]
            max_value = value[i]*(capacity/weight[i])
            break
    return max_value

if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    value = data[2:(2 * n + 2):2]
    weight = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weight, value)
    print("{:.10f}".format(opt_value))