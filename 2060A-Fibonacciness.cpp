#include <bits/stdc++.h>
using namespace std;

const int N = 6;

int fab(vector<int> arr, int a){
    int cnt = 0;
    arr[3] = a;
    for(int i=3; i<N; i++){
        if(arr[i-1] + arr[i-2] == arr[i]){
            cnt ++;
        }
    }
    return cnt;
}

int solve(){
    vector<int> arr (N, 0);

    for(int i=1; i<N; i++){
        if(i != 3) cin >> arr[i];
    }

    return max(fab(arr, arr[4] - arr[2]), fab(arr, arr[1] + arr[2]));
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    int t; cin >> t;

    while(t--){
        cout << solve() << endl;
    }
}
