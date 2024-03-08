'''
TC:     O(n)
SC:     O(1)
Link:   https://codeforces.com/problemset/problem/1917/A
'''

def minProduct(arr, n):
    nCnt = 0
    
    for a in arr:
        if 0 == a:
            print(0)
            return
        if a < 0:
            nCnt += 1

    if 0 == nCnt%2:
        print(f'{1}\n{1} {0}')
    else:
        print(0)
    
def main():
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        arr = list(map(int, input().strip().split()))
        minProduct(arr, n)
    
if __name__ == '__main__':
    main()