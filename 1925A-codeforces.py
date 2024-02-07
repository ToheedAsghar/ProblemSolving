# Link: https://codeforces.com/problemset/problem/1925/A
'''
TC: O(t*n)
SC: O(t*n)
'''
string = "abcdefghijklmnopqrstuvwxyz"
def subsequenceString(n,k):
    str = ""
    for i in range(0,n):
        str += string[0:k]
    return str

t = int(input())
while t>0:
    n,k = map(int, input().split())
    print(subsequenceString(n,k))
    t -= 1




