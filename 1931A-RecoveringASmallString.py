'''
TC:     O(1) for each test case
SC:     O(1)
Link:   https://codeforces.com/problemset/problem/1931/A
'''
def smallString(n):
    retStr = ''
    if n<=26:
        retStr += 'aa'
        retStr += chr(n - 2 + 96)
    elif n <= 52:
        retStr = 'a'
        n = n-1
        t = n % 26
        if(0 == t):
            retStr += 'ay'
        else:
            retStr += chr(t + 96)
            n -= t
            retStr += chr(n + 96)
    else:
        t = n%26
        if(0 == t):
            retStr = 'zzz'
        else:
            retStr = chr(t + 96)
            retStr += 'zz'
        
    return retStr

t = int(input())
while t != 0:
    n = int(input())
    print(smallString(n))  
    t -= 1
'''
5
24
70
3
55
48
aav
rzz
aaa
czz
auz
'''