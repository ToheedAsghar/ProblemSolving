// https://codeforces.com/problemset/problem/580/C
#include <bits/stdc++.h>
using namespace std;

set<int> cats;
set<int> visited;

void solve(const vector<vector<int>>& edges, int m, int c, int& cnt, int currentNode){
    if(cats.find(currentNode) == cats.end()){
        c = 0;
    }
    else{
        ++c;
    }

    // base case
    if(c > m){
        return;
    }

    if(currentNode != 1 and edges[currentNode].size() == 1){
        cnt++;
        return;
    }

    visited.insert(currentNode);
    for(const auto& node: edges[currentNode]){
        if(visited.find(node) == visited.end()){
            solve(edges, m, c, cnt, node);

        }
    }
    visited.erase(currentNode);
}

int main(){
    int n , m;
    cin >> n >> m;

    for(int i=1; i<=n ; i++){
        int temp; cin >> temp;
        if(temp == 1) { cats.insert(i); }
    }

    vector<vector<int>> edges (n+1, vector<int>());
    for(int i=1; i<n; i++){
        int u, v;
        cin >> u >> v;
        edges[u].push_back(v);
        edges[v].push_back(u);
    }

    int cnt = 0, c = 0;
    solve(edges, m, c, cnt, 1);
    cout << cnt << endl;

    return 0;
}
