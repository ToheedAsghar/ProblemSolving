// https://codeforces.com/problemset/problem/2124/B

#include <bits/stdc++.h>
using namespace std;

void solve()
{
    // function body
    int n;
    cin >> n;
    int m = INT_MAX;
    vector<int> arr(n, 0);
    for (int i = 0; i < n; i++)
    {
        cin >> arr[i];
    }

    int s = arr[0];
    if (2 == n) {
        s += (arr[0] < arr[1])? arr[0] : arr[1];
    }
    else
    {
        int b = min(arr[0], arr[1]);
        s += b;
    }

    cout << s << "\n";
}

int main()
{
    int t;
    cin >> t;

    while (t--)
    {
        solve();
    }
}
