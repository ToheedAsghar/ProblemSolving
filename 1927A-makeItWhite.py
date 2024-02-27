'''
TC:     O(n)
SC:     O(1)
Link:   https://codeforces.com/problemset/problem/1927/A
'''
def makeItWhite(fence: str, n: int) -> int:
    left: int = 0
    right: int = n-1
    
    while fence[left] != 'B':
        left += 1
    while fence[right] != 'B':
        right -= 1
    
    return right-left + 1

def main() -> None:
    t:int = int(input())
    for _ in range(t):
        n: int = int(input())
        fence: str = input().strip()
        print(makeItWhite(fence,n))
    
if __name__ == '__main__':
    main()