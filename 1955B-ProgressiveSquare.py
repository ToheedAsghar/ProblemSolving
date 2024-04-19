# https://codeforces.com/problemset/problem/1955/B

from collections import Counter

def progressiveCheck(n, c, d, inputList):
    grid = [[0 for _ in range(n)] for _ in range(n)]
    hashmap = Counter(inputList)

    grid[0][0] = min(inputList)
    del hashmap[grid[0][0]]
    
    for i in range(n):
        if 0 != i:
            ele = grid[i-1][0] + c
            if ele in hashmap:
                grid[i][0] = ele
                hashmap[ele] -= 1
                if 0 == hashmap[ele]:
                    del hashmap[ele]
            else:
                return False

        for j in range(1, n):
            ele2 = grid[i][j-1] + d
            if ele2 in hashmap:
                grid[i][j] = ele2 
                hashmap[ele2] -= 1
                if 0 == hashmap[ele2]:
                    del hashmap[ele2]
            else:
                return False

    return True


def main():
    t = int(input().strip())
    for _ in range(t):
        n, c, d = map(int, input().split())
        inputList = list(map(int, input().strip().split()))[:n*n]
        print('Yes') if progressiveCheck(n, c, d, inputList) else print('No')

if __name__ == '__main__':
    main();
