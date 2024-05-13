def contestProposal(a, b, n):
    i = 0
    j = 0
    cnt = 0
    while j < n:
        if a[i] > b[j]:
            cnt += 1
        else:
            i += 1
        j += 1
    return cnt


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))[:n]
        b = list(map(int, input().split()))[:n]

        cnt = contestProposal(a, b, n)
        print(cnt)
      
