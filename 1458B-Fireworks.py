def fireworks(a, b, m):
   return m//a + m//b + 2

def main():
    t = int(input())
    for _ in range(t):
        a, b, m = map(int, input().strip().split())
        print(fireworks(a, b, m))

if __name__ == '__main__':
    main()
