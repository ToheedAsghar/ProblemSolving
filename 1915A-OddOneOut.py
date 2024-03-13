'''
TC:     O(1)
SC:     O(1)
Link: https://codeforces.com/problemset/problem/1915/A
'''

def main() -> None:
    t = int(input())
    for _ in range(t):
        a, b, c = map(int, input().strip().split())
        if a == b:
            print(c)
        elif a == c:
            print(b)
        else:
            print(a)


if __name__ == '__main__':
    main()
