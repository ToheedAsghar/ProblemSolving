#include <iostream>
#include <vector>
#include <algorithm>

#define ll long long int

using namespace std;

void solve(){
    int n; cin >> n;
    vector<int> arr(n);
    for(int i=0; i<n; i++){
        cin >> arr[i];
    }

    ll evenSum = 0;
    ll oddSum = 0;

    bool odd = true;

    for(int i=0; i<n; i++){
        if(arr[i]%2){
            oddSum += (arr[i]-1);
            odd = false;
        } else{
            evenSum += arr[i];
        }
    }

    if(evenSum == 0 or odd){
        cout << *max_element(arr.begin(), arr.end()) << "\n";
    } else{
        cout << evenSum + oddSum + 1 << "\n";
    }
}

int main(){
    int t; cin >> t;
    while(t--){
        solve();
    }
}
