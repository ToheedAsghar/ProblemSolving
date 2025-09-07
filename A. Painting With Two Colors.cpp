// https://codeforces.com/problemset/problem/2134/A

#include <iostream>

using namespace std;

void fastIO() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
}

void solve() {

    int n , a, b;
    cin >> n >> a >> b;

    if(n%2){ // odd case
        if(0==a%2 and b%2 and b>a){
            cout << "yes" << endl;
        } else {
            cout << (0 == a%2 or 0 == b%2? "No" : "Yes") << endl;
        }
    } else{ // even case
        if(a%2 and 0 == b%2 and b>a ){
            cout << "yes" << endl;
        } else {
            cout << ((a%2 or b%2)? "No" : "Yes") << endl;
        }
    }
}

int main() {
    fastIO();
    
    int t;
    cin >> t;
    while (t--) {
        solve();
    }
    
    return 0;
}
