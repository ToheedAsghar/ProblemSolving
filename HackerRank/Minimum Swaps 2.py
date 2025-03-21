from typing import List

def minimumSwaps(arr) -> None:
    n: int = len(arr)
    inds: List[int] = [0] * n
    minSwaps: int = 0

    for i in range(n):
        arr[i] -= 1
        inds[arr[i]] = i

    for i, a in enumerate(arr):

        if inds[i] != i:
            arr[i], arr[inds[i]] = arr[inds[i]], arr[i]
            minSwaps += 1
            inds[a] = inds[i]
            
    return minSwaps

def main() -> None:
    n: int = int(input().strip())
    arr: List[int] = list(map(int, input().split()))

    print(minimumSwaps(arr=arr))

if __name__ == '__main__':
    main()
