from random import randint, randrange

def max_pairwise_product_fast(n, a):
    #n = int(input())
    #a = [int(x) for x in input().split()]

    index1 = 0
    for i in range(1, n):
        if a[i] > a[index1]:
            index1 = i
    if index1 == 0:
        index2 = 1
    else:
        index2 = 0
    for j in range(1, n):
        if a[j] > a[index2] and j != index1:
            index2 = j

    return a[index1]*a[index2]

def max_pairwise_product(n, a):
    #n = int(input())
    #a = [int(x) for x in input().split()]

    max_product = 0
    for first in range(n):
        for second in range(first + 1, n):
            max_product = max(max_product,
                a[first] * a[second])

    return max_product

# stress test
def stress_test(N, M):
    while True:
        N = randint(0, 9) + 2
        a = []
        for i in range(N):
            a.append(randrange(0, M))
    
        print(a)
        res1 = max_pairwise_product_fast(N, a)
        res2 = max_pairwise_product(N, a)
        if res1 == res2:
            print("OK", res1)
            continue
        else:
            print("Wrong", res1, res2)
            break
stress_test(10, 100)
        