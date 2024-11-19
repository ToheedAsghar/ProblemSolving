// https://codeforces.com/problemset/problem/2004/B

#include <iostream>
using namespace std;

void solve(){
	int l, r, R, L, cnt;
	
	cin >> l >> r;
	cin >> L >> R;

	cnt = min(r, R) - max(L, l) ;
	if(cnt < 0) cnt = 1;
	else{
		cnt += l != L;
		cnt += R != r;
	}
	
	cout << cnt << '\n';
}

int main(){
		int t;
		cin >> t;
		while(t--)
			solve();
	
}
