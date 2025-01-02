#https://codeforces.com/problemset/problem/208/d
def solve(arr, wPoints, pCnt, points):

    for p in arr:
        points += p
        for i in range(4, -1, -1):
            if points >= wPoints[i]:
                div =  points // wPoints[i]
                pCnt[i] += div
                points -= div * wPoints[i]

    for val in pCnt:
        print(val, end=' ')
    print()
    print(points)


def main() -> None:
    n = int(input().strip())
    arr = list(map(int, input().split()))[:n]
    wPoints = list(map(int, input().split()))[:5]

    solve(arr, wPoints, [0, 0, 0, 0, 0], 0)


if __name__ == '__main__':
    main()
