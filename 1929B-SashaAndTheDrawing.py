'''
TC:         O(1)
SC:         O(1)
Link:       https://codeforces.com/problemset/problem/1929/B
'''

import math         # math.ceil
# Sasha and the Drawing


def minCells(n: int, k: int) -> int:
    diagonals: int = 4*n - 2
    if(diagonals == k):
        return 2*n
    else:
        return math.ceil(k/2)
    
    
def main() -> None:
    t: int = int(input().strip())
    for _ in range(t):
        n,k = map(int, input().split())
        print(minCells(n, k))
    

if __name__ == '__main__':
    main()
