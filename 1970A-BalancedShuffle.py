# https://codeforces.com/problemset/problem/1970/A1

def balanceParenthesis(par):
    prefixBalance = [0]
    n = len(par)
    hm = {')': -1, '(': 1}

    position = [x for x in range(1, n+1)]

    for i in range(1, n):
        temp = prefixBalance[-1] + hm[par[i-1]]
        prefixBalance.append(temp)

    zipped = list(zip(prefixBalance, position, par))
    zipped.sort(key=lambda x: (x[0], -x[1]))

    _, position, par = zip(*zipped)
    return ''.join(par)
    

if __name__ == '__main__':
    par = input().strip()
    print(balanceParenthesis(par))
