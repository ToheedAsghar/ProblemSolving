# https://codeforces.com/problemset/problem/1922/A

def trickyTemplate(a,b,c) -> bool:
    n =len(a)
    for i in range(n):
        if a[i] != c[i] and b[i] != c[i]:
            return True;
    return False;

n = 0
t = 0;
t = int(input())

while(t != 0):
    n = input()
    a,b,c = "", "", ""
    a = input()
    b = input()
    c = input()

    retVal = trickyTemplate(a,b,c)
    if retVal == True:
        print("YES")
    else:
        print("NO")
    t = t - 1


