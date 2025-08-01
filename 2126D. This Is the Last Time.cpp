#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>

using namespace std;

void solve(){
    int n , k;
    cin >> n >> k;
    vector<vector<int>> arr(n, vector<int>(3, 0));

    for(int i=0; i<n; i++){
        int a , b, c;
        cin >> a >> b >> c;

        arr[i][0] = a; arr[i][1] = b; arr[i][2] = c;
    }

    sort(arr.begin(), arr.end());

    int maxValue = INT_MIN;
    for(int i=0; i<n; i++){
        if(arr[i][0] > k ) break;

        if(arr[i][0] <= k and k <= arr[i][1]){
            k = maxValue = max(k, arr[i][2]);
        }
    }
    
    cout << k << "\n";
}

int main(){
    int t;
    cin >> t;

    while(t--){
        solve();
    }
}
