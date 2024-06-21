# TC: O(N)

def shiftAndSort(s):
    cost = 0
    i = 0
    n = len(s)
    
    while i < n and '0' == s[i]:
        i += 1
    
    j = i + 1
    while j < n:
        if '0' == s[j]:
            cost += (j - i + 1)
            i += 1
        j += 1
        
    return cost
        
            
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        print(shiftAndSort(s))
