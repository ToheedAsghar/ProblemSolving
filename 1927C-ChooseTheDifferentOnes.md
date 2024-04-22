# [1927C - Choose the Different Ones](https://codeforces.com/contest/1927/problem/C)

The problem is to analyze both the arrays and hve to pick exackly k//2 elements from each of the lists. 

```python3

def differentOnes(a, b, k):
    seta = set(a)
    setb = set(b)

    a_cnt, b_cnt = 0, 0
    for i in range(1, k+1):
        if i in seta and i in setb:
            continue
        elif i in seta:
            a_cnt += 1
        elif i in setb:
            b_cnt += 1
        else:
            return False
    return True if a_cnt <= k//2 and b_cnt <= k//2 else False

def main():
    t = int(input().strip())
    for _ in range(t):
        n, m, k = map(int, input().strip().split())
        a = list(map(int, input().strip().split()))[:n]
        b = list(map(int, input().strip().split()))[:m]

        print('Yes') if differentOnes(a, b, k) else print('No')

if __name__ == '__main__':
    main()

```

## Time Complexity 

- Creating sets seta and setb takes O(n + m) time, where n is the length of list a and m is the length of list b.
- The loop iterates from 1 to k. Inside the loop, there are constant time operations.
- However, the in operation on sets has an average time complexity of O(1). So, the overall time complexity of the loop is O(k) * O(1) = O(k).
- Therefore, the overall time complexity of the code is **O(n + m + k)**, where n is the length of list a, m is the length of list b, and k is the maximum value from the input.

## Space Complexity

*seta* and *setb* store unique elements from lists a and b, respectively. So, the space complexity for creating these sets is **O(n + m)**, where n is the length of list a and m is the length of list b.
