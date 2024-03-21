# A. Shuffle Party

Analyzing the pattern upto n = 0. The index of 1 changes when n = [1, 2, 4, 8, 16, 20]. Which gives the pattern that index of 1 changes when the n is power of 2.

## PseudoCode

```
procduct <- 1
if product = n then return product
if product*2 <= n then call repeat the process with product = product * 2
else return product
```

## Code

```python
def shuffleParty(product, n):
    if product == n:
        return product
    
    elif product*2 <= n:
        return shuffleParty(product*2, n)
    else:
        return product
    
def main() -> None:
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        print(shuffleParty(1, n))
    
if __name__ == '__main__':
    main()
```

##  Time Complexity:

- The function recursively doubles the product until it reaches a value greater than n.
- The number of recursive calls required to reach a value greater than n is logarithmic (base 2) with respect to n.
- Therefore, the time complexity of this function is O(log n).

## Space Complexity:

- Each recursive call consumes space on the call stack.
- Since the function makes recursive calls until product*2 exceeds n, the maximum depth of recursion is logarithmic (base 2) with respect to n.
- As a result, the space complexity of this function is O(log n).

**Note**: The space complexity can be minimized to O(1) by using a while loop.
