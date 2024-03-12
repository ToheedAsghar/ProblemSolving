'''
TC:     O(n)
SC:     O(n)
Link:   https://codeforces.com/problemset/problem/1914/A
'''


def solve(arr, n):
    dict = {}
    for i in arr:
        dict[i] = dict.get(i, 0) + 1
    
    cnt = 0
    for key,value in dict.items():
        if key in dict and dict[key] >= (ord(key) - 65) + 1:
            cnt += 1
    
    return cnt


def main():
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        arr = input().strip()
        print(solve(arr, n))
        
        
if __name__ == '__main__':
    main()
 
