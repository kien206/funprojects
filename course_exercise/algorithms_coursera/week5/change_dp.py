# Uses python3
import sys

def get_change(coins, m):
    if m == 0:
        return 0
    if min(coins) > m:
        return -1
    dp = [-1 for i in range(m+1)]
    for i in coins:
        if i > len(dp)-1:
            continue
        dp[i] = 1
        for j in range(i+1, m+1):
            if dp[j-i] == -1:
                continue
            elif dp[j] == -1:
                dp[j] = dp[j-i] + 1
            else:
                dp[j] = min(dp[j], dp[j-i]+1)
    return dp[m]
coins = [1,3,4]
'''print(get_change(coins, 50))'''
if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(coins, m))

