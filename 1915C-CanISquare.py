'''
TC:     O(n)
SC:     O(1)
Link:   https://codeforces.com/problemset/problem/1915/C
'''

import math


def canMakeSqaure(sum):
    t = math.isqrt(sum)
    return 'YES' if t * t == sum else 'NO'


def main() -> None:
    t = int(input().strip())
    
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        print(canMakeSqaure(sum(arr)))
    
    
if __name__ == '__main__':
    main()
