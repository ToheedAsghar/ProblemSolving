'''
TC:     O(n)
SC:     O(1)
Link:   https://codeforces.com/problemset/problem/1919/B
'''

def plusMinusSplit(str, n):
    pcnt = 0
    ncnt = 0
    
    for i in str:
        if '+' == i:
            pcnt += 1
        else:
            ncnt += 1
    
    return abs(pcnt-ncnt)

def main():
    t = int(input())
    for _ in range(t):
        n = int(input().strip())
        str = input().strip()
        print(plusMinusSplit(str, n))

if __name__ == '__main__':
    main()