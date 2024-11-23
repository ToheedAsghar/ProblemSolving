// https://codeforces.com/contest/977/problem/E
#include <bits/stdc++.h>
using namespace std;

vector<int>degree;
set<int> comp;
set<int> visited;

void dfs(const vector<vector<int>>& edges,const int i){
    if(visited.find(i) != visited.end()) return;

    visited.insert(i);
    comp.insert(i);
    for(const auto& u: edges[i]){
        if(visited.find(u) == visited.end()){
            dfs(edges, u);
        }
    }
}

int main(){
    int n, m;
    cin >> n >> m;

    vector<vector<int>> edges(n+1, vector<int>());
    degree = vector<int> (n+1, 0);

    for(int i=0; i<m; i++){
        int u, v;
        cin >> u >> v;

        edges[u].push_back(v);
        edges[v].push_back(u);

        degree[u]++;
        degree[v]++;
    }

    int cnt = 0;
    for(int i=1; i<=n; i++){
        if(visited.find(i) != visited.end()){
            continue;
        }

        comp.clear();
        dfs(edges, i);

        bool flag = true;

        for(const auto& it: comp){
            if(degree[it] != 2) flag = false;
        }

        cnt += flag;
    }

    cout << cnt << endl;

}
