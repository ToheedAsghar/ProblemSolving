'''
TC:     O(nlogn)
SC:     O(n)
Link:   https://codeforces.com/problemset/problem/1918/B

'''

def solve(a,b):
    combine = list(zip(a,b))
    combine.sort(key= lambda x: x[0])
    a, b = zip(*combine)
    
    for n in a:
        print(n, end=' ')
    print()
    for n in b:
        print(n, end=' ')

def main() -> None:
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        a = list(map(int, input().strip().split()))
        b = list(map(int, input().strip().split()))
        solve(a,b)

if __name__ == '__main__':
    main()