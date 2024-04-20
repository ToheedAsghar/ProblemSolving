## [A. Nene's Game](https://codeforces.com/problemset/problem/1956/A)

We've a list of indexes and we've to exclude these indeces from the list every time until no such index exists in the list. One more thing that this indices list is sorted in non-decreasing order. By this we get the first lead that is the key to our time complexity effiecieny. That is, if i've a list *[3, 7, 11, 15]*. The relations is that if my list doesn't contains 3, then it's obvious that the list will not contain any of the numbers on the right of the number 3.


## Python Code

```python

def binarySearch(l, r, n):
    if l > r:
        return -1

    mid = (l+r) // 2
    if mid == n:
        return mid
    elif mid > n:
        return binarySearch(l, mid-1, n)
    else:
        return binarySearch(mid+1, r, n)

def nenesGame(k, q, a, n):
    result = []

    for ele in n:
        flag = binarySearch(1, ele, a[0])
        if -1 != flag:
            result.append(a[0]-1)
        else:
            result.append(ele)
    
    for ele in result:
        print(ele, end=' ')
    print()

def main():
    t = int(input().strip())
    for _ in range(t):
        k, q = map(int, input().strip().split())
        a = list(map(int, input().strip().split()))[:k]
        n = list(map(int, input().strip().split()))[:q]

        nenesGame(k, q, a, n)

if __name__ == "__main__":
    main()

```

## Time Complexity

Time Complexity: The time complexity of the binarySearch function is O(log n), where n is the size of the array being searched. This is because the function performs a binary search, which halves the search space with each iteration. The nenesGame function performs a binary search for each element in the n list, which has a size of q. Therefore, the time complexity of nenesGame is O(q * log a), where a is the maximum value of the a list. The main function performs a binary search for each element in the n list for each test case. Therefore, the time complexity of main is O(t * q * log a), where t is the number of test cases.

# Space Complexity

The binarySearch function has a space complexity of O(1), as it only uses a constant amount of additional space to store the l, r, and mid variables. The nenesGame function has a space complexity of O(q), as it stores the results of the binary searches in the result list. The main function has a space complexity of O(t * q), as it stores the results of the nenesGame function for each test case. Therefore, the overall time complexity of the code is O(t * q * log a), and the overall space complexity is O(t * q).
