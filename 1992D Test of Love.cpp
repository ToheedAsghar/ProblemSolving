// Solution of: https://www.youtube.com/watch?v=9Vv2ZukG1CM&t=2861s

#include <iostream>
#include <cassert>

using namespace std;

void runCase(){
    int n, m, k;
    cin >> n >> m >> k;
    string river;
    cin >> river;

    river = "L" + river + "L";

    int current = 0, swim = 0;

    while(current <= n){
        if(river[current] == 'C'){
            break;
        }
        if(river[current] == 'W'){
            swim ++;
            current += 1;
            continue;
        }
        
        assert(river[current] == 'L');
        bool jumped = false;

        for(int i = min((current + m), n+1); i > current; i--){
            if(river[i] == 'L'){
                jumped = true;
                current = i;
                break;
            }
        }

        if(jumped) continue;

        // not jumped
        for(int i = min((current + m), n+1); i > current; i--){
            if(river[i] == 'W'){
                jumped = true;
                current = i;
                break;
            }
        }

        if(!jumped) break;
    }

    cout << ((current > n and swim <= k)? "YES" : "No") << endl;
}

int main(){
    int t;
    cin >> t;

    while (t--){
        runCase();
    }
}
