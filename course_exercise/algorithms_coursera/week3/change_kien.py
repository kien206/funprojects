# Uses python3
import sys

def get_change(m):
    n = 0
    if m >= 10:
        while m/10 >= 1:
            m = m -10
            n += 1
            if 10 > m >=5:
                m -= 5
                n += 1
                while 0 <m <5:
                    m -= 1
                    n += 1
            else:
                while 0 < m < 5:
                    m -= 1
                    n += 1
    elif m <10 and m>= 5:
        m -= 5
        n += 1
        while 0 < m < 5:
            m -= 1
            n += 1
    else:
        while 0 < m <5:
            m -= 1
            n += 1
    return n

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
