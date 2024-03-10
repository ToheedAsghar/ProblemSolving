def maxCost(cost, labels, dailyCount):
    currCost = 0
    dc = 0
    retVal = float('-inf')
    
    for c,l in zip(cost, labels):
        currCost += c
        
        if 'illegal' == l:
            continue
        
        dc += 1
        
        if dc == dailyCount:
            retVal = max(retVal, currCost)
            currCost = 0
            dc = 0
    
    return retVal

def main() -> None:
    cost = [0, 3, 2, 3, 4]
    labels = ["legal", "legal", "illegal", "legal", "legal"]
    dailyCount = 1
    print(maxCost(cost, labels, dailyCount))
            
if __name__ == '__main__':
    main()
        
