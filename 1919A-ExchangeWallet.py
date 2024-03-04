'''
TC:     O(1)
SC:     O(1)
Link:   https://codeforces.com/problemset/problem/1919/A
'''

def walletExchange(a,b):
    if (0 == a%2 and 0 == b%2) or (0 != a%2 and 0!= b%2):
        return 'Bob'
    else:
        return 'Alice'


def main():
    t = int(input().strip())
    for _ in range(t):
        a,b = map(int, input().strip().split())
        print(walletExchange(a,b))
        
        
if __name__ == '__main__':
    main()