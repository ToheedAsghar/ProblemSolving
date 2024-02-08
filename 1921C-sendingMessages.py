# Link https://codeforces.com/problemset/problem/1921/C

'''
TC: O(n)
SC: O(n)
'''

def canSendMessages(n,f,a,b,msgs):
    diff = 0
    for i in range(n):
        t = (msgs[i] - diff) * a
        if t <= b:
            f -= t
        else:
            f -= b
        diff = msgs[i]

    return f > 0


t = int(input())
while t != 0:

    n,f,a,b = map(int, input().split())
    msgs = [int(x) for x in input().split()]

    print("YES" if canSendMessages(n,f,a,b,msgs) else "NO")

    t = t-1

'''
If the (diff*a) is greater than b, the it's better to shutdown the phone,
than to wait for the moment.
'''