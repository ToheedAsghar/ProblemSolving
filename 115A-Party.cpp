// https://codeforces.com/problemset/problem/115/A
#include <bits/stdc++.h>
using namespace std;

int solve(const vector<vector<int>>& edges, vector<int>& dp, const int& N, int i){
    if(i > N){ return 0; }
    if(dp[i] != -1) { return dp[i]; }

    int steps = 1;
    for(const auto& ele: edges[i]){
        steps = max(steps, 1 + solve(edges, dp, N, ele));
    }

    return dp[i] = steps;
}

int main(){
    int N;
    cin >> N;

    vector<int> im(N+1, -1);
    for(int i=1; i<=N; i++){
        cin >> im[i];
    }

    vector<vector<int>> edges(N+1, vector<int>());
    for(int i=1; i<=N; i++){
        if(im[i] != -1){
            edges[im[i]].push_back(i);
        }
    }

    // for(const auto& row: edges){
    //     for(const auto& ele: row){
    //         cout << ele << ' ';
    //     } cout << '\n';
    // }

    vector<int> dp (N+1, -1);

    for(int i=1; i<=N; i++){
        solve(edges, dp, N, i);
    }

    // for(const auto& e: dp){
    //     cout << e << ' ';
    // } cout << endl;

    cout << *max_element(dp.begin(), dp.end()) << endl;

}
