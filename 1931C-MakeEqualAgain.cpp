/*
TC:     O(n)
SC:     O(1)
Link:   https://codeforces.com/problemset/problem/1931/C
*/
#include<iostream>
#include<vector>
#include<cmath>
#include <climits>
using namespace std;

int minOperations(const vector<int>& arr,const int& n) {
    // Checking from the Start
	int st = -1;
	int end = -1;
	int x = arr[0];
	for (int i = 0; i < n; i++) {
		if (arr[i] == x) {
			continue;
		}
		else if (-1 == st) {
			st = end = i;
		}
		else {
			end = i;
		}
	}
	int ans1 =  (-1 == end) ? 0 : (end - st) + 1;

    // Checking from the End
	st = -1;
	end = -1;
	x = arr[n - 1];
	for (int i = n - 1; i >= 0; i--) {
		if (arr[i] == x) {
			continue;
		}
		else if (-1 == st) {
			st = end = i;
		}
		else {
			end = i;
		}
	}
	int ans2 = (-1 == end) ? 0 : (st - end) + 1;
    
    // Returning the minimum Operations 
	return min(ans1, ans2);
}

int main() {
    int t;
    cin >> t;
    while(t--){
        int n;
        cin >> n;
        vector<int> arr(n);
        for(int i=0; i<n; i++){
            cin >> arr[i];
        }
        cout << minOperations(arr, n) << '\n';
    }
	return 0;
}