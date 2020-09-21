#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
#define ll long long int


int main() {
vector<pair<int, int>> array;
ll n, x, y, count = 0, cur_val = 0;

cin >> n;
for (ll i = 0; i < n; i++) {
	cin >> x >> y;
	array.push_back(make_pair(y, x));
}

// Greedy Algorithm : order by earlier finishing times
sort(array.begin(), array.end());

for (auto element : array) {
	if (element.second >= cur_val) {
		cur_val = element.first;
		count++;
	}
}
cout << count;
	
}
