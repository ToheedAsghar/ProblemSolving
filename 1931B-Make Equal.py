'''
TC:     O(n) for each test case
SC:     O(1)
Link:   https://codeforces.com/problemset/problem/1931/B

'''
def canFill(n, list):
    amm = sum(list) // n
    ext = 0
    for i in range(n):
        if list[i] == amm:
            pass
        elif list[i] > amm:
            ext += list[i] - amm
        else:
            t = amm - list[i]
            ext -= t
        
        if ext < 0:
            return False

    return True if (ext == 0) else False

t = int(input())
for _ in range(t):
    n = int(input())
    list = [int(x) for x in input().split()]
    print("YES" if canFill(n, list) else "NO")


'''
6
1
43
2
1 3
5
4 5 2 1 3
3
1 2 3
7
4 5 5 0 6 4 4
7
6 5 5 1 3 4 4
'''