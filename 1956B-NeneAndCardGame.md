# [1956B - B. Nene and the Card Game](https://codeforces.com/problemset/problem/1956/B)

In this Problem, we just hvae to analyze how many duos we have. In this case, the point is ours as there is not other way Nene can have that card as there are only two cards. If both players play optimaally, then our total points will be the number of pairs we have.

## Python Code

```python3

from collections import Counter

def cardGame(a):
    dict = Counter(a)
    
    cnt = 0
    for value in dict.values():
        if 2 == value:
            cnt += 1

    return cnt

def main():
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        a = list(map(int, input().strip().split()))[:n]
        print(cardGame(a))

if __name__ == '__main__':
    main()

```

## Time Complexity:

- The time complexity of creating a Counter object using Counter(a) is O(n), where n is the number of elements in the input list 'a'.
- The loop that iterates over the values in the dictionary has a time complexity of O(n), where n is the number of unique elements in the input list 'a'.
- Within this loop, the comparison if 2 == value and incrementing cnt are constant time operations.
- Overall, the time complexity of the cardGame function is O(n), where n is the number of elements in the input list 'a'.
- The main function reads input values and calls cardGame function for each test case, so the time complexity of the main function is also O(n).

Therefore, the overall time complexity of the provided code is **O(n)**, where n is the number of elements in the input list 'a'.

## Space Complexity

- The space complexity of creating a Counter object using Counter(a) is O(n), where *n* is the number of elements in the input list 'a'.
- Additional space is used for the dictionary 'dict' and the variable 'cnt', both of which are constant space.
- The space complexity of the cardGame function is O(n) due to the Counter object.
- The space complexity of the main function is also O(n) due to the input list 'a'.

Therefore, the overall space complexity of the provided code is **O(n)**, where *n* is the number of elements in the input list 'a'.
