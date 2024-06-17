def xorSequences(x, y):
    z = x ^ y

    cnt = 0
    while not z & 1:
        z = z >> 1
        cnt += 1

    ans = 1
    for _ in range(cnt):
        ans = ans << 1

    return ans

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        x, y = map(int, input().split()) 

        print(xorSequences(x, y))
