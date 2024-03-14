# [Rudolf and the Ticket](https://codeforces.com/problemset/problem/1941/A) 

## Time Complexity:

The given Python function ***countWays(b, c, k)*** has a time complexity of **O(n * m)**, where n and m are the lengths of the lists b and c respectively.
The function iterates over the elements of both lists using nested loops, resulting in a time complexity that is proportional to the product of the lengths of the lists.

## Space Complexity:

The space complexity of the ***countWays(b, c, k)*** function is **O(1)**, as it only uses a constant amount of additional space to store the variable cnt, which is an integer.
The function does not create any additional data structures or lists, so the memory usage remains constant regardless of the input size.

## Explanation:
The Problem is simple, just iterate through both lists and check whether the combination a + b <= k. If yes, store increment the *cnt* variable. After iterations, return the *cnt* as
the number of minimum number of coins Rudolf can pickup coins.

## Program

```python
def countWays(b, c, k):
    n = len(b)
    m = len(c)

    cnt = 0
    for i in range(n):
        for j in range(m):
            if b[i] + c[j] <= k:
                cnt += 1

    return cnt

def main() -> None:
    t = int(input().strip())
    for _ in range(t):
        n, m, k = map(int, input().strip().split())
        b = list(map(int, input().strip().split()))
        c = list(map(int, input().strip().split()))
        print(countWays(b, c, k))

if __name__ == '__main__':
    main()

```
