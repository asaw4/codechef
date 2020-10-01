#include<bits/stdc++.h>

using namespace std;

int main(){

    int t;
    cin >> t;
    for(int ii=0; ii<t; ii++){

        int x,y,k,n;
        cin >> x >> y >> k >> n;
        int prr[n], crr[n];
        for(int i=0; i<n; i++){
            cin >> prr[i];
            cin >> crr[i];
        }

        int pages_needed = x-y;
        bool ans = false;
        for(int i=0; i<n; i++){
            if(prr[i]>=pages_needed && crr[i]<=k){
                ans = true;
                break;
            }
        }

        if(ans)
            cout << "LuckyChef" << endl;
        else
            cout << "UnluckyChef" << endl;

    }


    return 0;
}
