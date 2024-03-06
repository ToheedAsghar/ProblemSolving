'''
TC:     O(1)
SC:     O(1)
Link:   https://codeforces.com/problemset/problem/1918/A
'''

def maximumStability(n, m):
    return n * (m//2)


def main():
    t = int(input().strip())
    for _ in range(t):
        n, m = map(int, input().strip().split())
        print(maximumStability(n, m))
        
    
if __name__ == '__main__':
    main()
 