#include <bits/stdc++.h>
using namespace std;

void solve(){
	int n; cin >> n;
	int k; cin >> k;

	map<int, int> mp;
	int b, c;
	for(int i=0; i<k; i++){
		cin >> b >> c;
		mp[b] += c;
	}

	vector<int> arr;
	for(const auto& it: mp){
		arr.push_back(it.second);
	}

	sort(arr.begin(), arr.end(), greater<int>());

	int sum = 0;
	for(int i=0; i<arr.size() && i < n; i++){
		sum += arr[i];
	}

	cout << sum << endl;


}

int main(){
	int t; cin >> t;
	while(t--) solve();
}
