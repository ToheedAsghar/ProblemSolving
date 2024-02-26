'''
TC:     O(1)
SC:     O(1)
Link:   https://codeforces.com/problemset/problem/1928/A
'''

def rectangeCuting(h:int, w:int) -> bool:
    # edge case
    if h%2 != 0 and w%2 != 0:
        return False

    if h%2 == 0:
        a = h//2
        b = w + w
        if a != h and a!=w:
            return True
    
    if w%2 == 0:
        a = h + h
        b = w//2
        if a != h and a!=w:
            return True
        
    return False

    

def main() -> None:
    t = int(input())
    for _ in range(t):
        h,w = map(int, input().split())
        print('YES' if rectangeCuting(h, w) else 'NO')

if __name__=='__main__':
    main()