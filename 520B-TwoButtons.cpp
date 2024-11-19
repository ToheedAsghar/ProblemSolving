// https://codeforces.com/problemset/problem/520/B
#include <bits/stdc++.h>
using namespace std;

int solveR(int steps, int n, int m){
    if(n == m){
        return steps;
    }
    else if(m < n){
        return solveR(steps+1, n, m+1);
    }
    else{
        if(m%2 == 0) return solveR(steps+1, n, m/2);
        else return solveR(steps+1, n, m+1);
    }
}

int main(){
    int n, m;
    cin >> n >> m;

    int steps = 0;
    cout << solveR(steps, n, m) << "\n";
}
