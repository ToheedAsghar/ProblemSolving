'''
TC:         O(nlogn)
SC:         O(1)
Link:       https://codeforces.com/problemset/problem/1929/A
Time:       00:00:09:34:40
'''
def maxBeauty(n, list):
    list.sort()
    sum = 0
    for i in range(1, n):
        sum += list[i] - list[i-1]
    return sum

t = int(input())
for _ in range(t):
    n = int(input())
    list = [int(x) for x in input().split()]
    print(maxBeauty(n, list))