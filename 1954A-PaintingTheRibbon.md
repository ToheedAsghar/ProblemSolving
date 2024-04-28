# [A. Painting the Ribbon](https://codeforces.com/contest/1954/problem/A)

## Analysis

For Alice to win, she had to paint the parts in such a way that bob can't paint all parts the same color. Bob will make all colors to one existing color, so we've to deal with m-1 colors. For Alice to win, the total frequency of every color should be greater than k. Using this idea here is the algorithm:

```
rem <- n % m
div <- n / m

if n is completely divisible by m then
  if k < div:
    print 'YES'
  else:
    print 'No'

if k < (div+1)*(rem-1) + (m-rem)*(div):
  print('YES'
print('NO')
```

## Python Code

```python
def canAlicePaint(n, m, k):
    rem = n % m
    div = n // m

    if 0 == rem:
        if k >= div*(m-1):
            return True
        else:
            return False
    else:
        if k >= (div+1)*(rem-1) + (m-rem) * div:
            return True
        else:
            return False

def main() -> None:
    t = int(input().strip())
    for _ in range(t):
        n, m, k = map(int, input().strip().split())
        print('No') if canAlicePaint(n, m, k) else print('YES')

if __name__ == '__main__':
    main()

```

***Note**: The Algorithm uses constant time and space.*
