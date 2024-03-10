def longestSubarray(arr):
    n = len(arr)
    maxValue = 1
    
    i = 0
    for i in range(0, n):
        dict = {}
        dict[arr[i]] = dict.get(arr[i], 0) + 1
        j = i + 1
        
        while j < n and abs(arr[i]-arr[j]) < 2:
            if arr[j] not in dict.keys():
                if len(dict) == 2:
                    break
                else:
                    dict[arr[j]] = 1
                    j += 1
            else:
                dict[arr[j]] += 1
                j += 1
                    
        maxValue = max(maxValue, j - i)
        i += 1
        
    return maxValue
                
    
def main() -> None:
    print(longestSubarray([3, 2, 2, 1]))

if __name__ == '__main__':
    main()
                
            
            
