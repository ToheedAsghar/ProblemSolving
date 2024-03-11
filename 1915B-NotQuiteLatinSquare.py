'''
TC:      O()
SC:      O(1)
Link:    https://codeforces.com/contest/1915/problem/B
'''

def main() -> None:
        t = int(input())    
        for _ in range(t):
            flagA = 0
            flagB = 0
            flagC = 0
            for _ in range(3):
                str = input().strip()
                for ch in str:
                    if ch == 'A':
                        flagA += 1
                    elif ch == 'B':
                        flagB += 1
                    elif ch == 'C':
                        flagC += 1
            if 3 != flagA:
                print('A')
            elif 3 != flagB:
                print('B')
            else:
                print('C')
                
        
    if __name__ == '__main__':
        main()
      
