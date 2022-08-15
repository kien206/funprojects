import sys

def gcd_Euclidian(a,b):
    if (b == 0):
        return a
    elif (a > b):
        a1 = a%b
        return gcd_Euclidian(b, a1)
    elif (a < b):
        b1 = b%a
        return gcd_Euclidian(a, b1)
    elif a == b:
        return a

if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(gcd_Euclidian(a, b))
