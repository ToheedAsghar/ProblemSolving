'''
TC:     O(1) for each test case because all loops have fixed bounds
        and doesn't depend on input size
SC:     O(1) Regardless of the input size, the memory required for
        these variables remains constant.
Link:   https://codeforces.com/problemset/problem/1921/A
'''
t = int(input())
while t != 0:
    x = [0] * 4
    y = [0] * 4
    for i in range(4):
        x[i], y[i] = map(int, input().split())
    
    k = s = x[0]
    for i in range(1, 4):
        if x[i] != s:
            s = x[i]
            break

    print(abs(k-s) * abs(k-s))
    t  -= 1