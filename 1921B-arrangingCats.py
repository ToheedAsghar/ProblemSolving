'''
TC:     O(n) for each test case
SC:     O(1)
Link:   https://codeforces.com/problemset/problem/1921/B
'''
def arrangeCats(a: str, b: str) -> int:
    neg,pos = (0,0)

    n = len(a)
    for i in range(n):
        if '0' == a[i] and '1' == b[i]:
            neg += 1
        elif '1' == a[i] and '0' == b[i]:
            pos += 1

    return max(neg, pos)

t = int(input())
while t != 0:
    n = int(input())
    a = input()
    b = input()
    print(arrangeCats(a,b))
    t -= 1