'''
TC:             O(n)
SC:             O(1)
Link:           https://codeforces.com/problemset/problem/1927/B
Description:    The inner loop (dictionary iteration) runs at most 26 times (for the 26 alphabets).
                A dictionary (char_count) to store the count of each alphabet. The
                maximum size of this dictionary is 26 (for the 26 alphabets). Therefore, the space complexity is O(1)
                (constant space) because the dictionary size does not depend on the input size.
'''
def traceString(arr):
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    j= 0          # to keep track of alphabets
    dict = {}
    n = len(arr)
    retString = ""
    for i in range(n):
        if 0 == arr[i]:
            dict[alphabets[j]] = dict.get(alphabets[j], 0) + 1
            retString += alphabets[j]
            j += 1
        else:
            for key,value in dict.items():
                if value == arr[i]:
                    retString += key
                    dict[key] += 1
                    break
    return retString

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))[:n]
        print(traceString(arr))
    
if __name__ == '__main__':
    main()