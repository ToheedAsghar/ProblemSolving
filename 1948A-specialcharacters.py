"""
TC:    O(t)
SC:    O(1)
LINK:  https://codeforces.com/problemset/problem/1948/A
"""

def specialCharacters(n):
    if 0 != n % 2:
        print('NO')
    else:
        flag = True
        print('YES')
        os = 'AA'
        for _ in range(n//2):
            print(os, end='')
            if flag:
                os = 'BB'
                flag = False
            else:
                flag = True
                os = 'AA'
        print()


def main():
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        specialCharacters(n)


if __name__ == '__main__':
    main() 
