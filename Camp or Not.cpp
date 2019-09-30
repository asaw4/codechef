#include<bits/stdc++.h>

using namespace std;

int main(){
	int tc;
	cin >> tc;
	for(int ii=0; ii<tc; ii++){
		int d,ar[31],q;
		cin >> d;
		for(int i=0; i<31; i++){
			ar[i] = 0;
		}
		for(int i=0; i<d; i++){
			int a;
			cin >> a;
			cin >> ar[a-1];
		}
		for(int i=1; i<31; i++){
			ar[i] = ar[i] + ar[i-1];
		}
		cin >> q;
		for(int i=0; i<q; i++){
			int a,b;
			cin >> a >> b;
			if(ar[a-1]>=b)
				cout << "Go Camp\n";
			else
				cout << "Go Sleep\n";
		}
	}
	return 0;
}
