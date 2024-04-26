def olp(arr: List[int], n: int) -> None:

    num1: int = 0
    num2: int = 0
    num3: int = 0

    i: int = 0
    while i < n:
        num1 += arr[i]
        i += 3
    
    i: int = 1
    while i < n:
        num2 += arr[i]
        i += 3

    i: int = 2
    while i < n:
        num3 += arr[i]
        i += 3
    
    print(num1, num2, num3)

def main() -> None:
    n: int = int(input().strip())
    arr: List[int] = list(map(int, input().strip().split()))
    olp(arr, n)

if __name__ == '__main__':
    main()
