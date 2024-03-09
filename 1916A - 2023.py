'''
TC:     O(n)
SC:     O(1)
Link:   https://codeforces.com/problemset/problem/1916/A
'''

def solve(n, k, arr):
    rem = 2023
    
    for i in arr:
        if rem%i != 0:
            print("No")
            return
        else:
            rem //= i
    
    print("Yes")
    print(rem, end=' ')
    for i in range(k-1):
        print(1, end=' ')
    print()


def main():
    t = int(input().strip())
    for _ in range(t):
        n, k = map(int, input().strip().split())
        arr = list(map(int, input().split()))[:n]
        solve(n, k, arr)
        
        
if __name__ == '__main__':
    main()
 
