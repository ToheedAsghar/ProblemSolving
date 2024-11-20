// https://codeforces.com/problemset/problem/2038/N
#include <bits/stdc++.h>
using namespace std;

void solve(){
    string exp;
    cin >> exp;

    assert(exp.size() == 3);

    int a = exp[0] - '0';
    int b = exp[2] - '0';

    cout << a << (a==b? "=" : (a<b? "<" : ">")) << b << endl;
}

int main(){
    int t; cin >> t;
    while(t--){
        solve();
    }
}
