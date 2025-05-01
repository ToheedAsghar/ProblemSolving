#include <bits/stdc++.h>
using namespace std;

void solve(){
    int n; cin >> n;

    vector<int> arr (n);
    for(int i=0; i<n; i++){
        cin >> arr[i];
    }

    // leftMax
    vector<int> leftMax(n, 0);
    int m = INT_MIN;
    for(int i=0; i<n; i++){
        m = max(arr[i], m);
        leftMax[i] = m;
    }

    vector<long long> result(n, 0);
    long long currSum = 0;
    for(int k = 0; k<n; k++){
        result[k] = currSum + leftMax[n-k-1];
        currSum += arr[n-k-1]; 
    }

    for(const auto& it: result){
        cout << it << ' ';
    } cout << "\n";
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);


    int t; cin >> t;

    while(t--){
        solve();
    }
}
